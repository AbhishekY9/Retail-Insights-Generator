from langchain_google_genai import GoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma
from langchain.prompts import FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX
from langchain.prompts.prompt import PromptTemplate
from few_shots import few_shots
import os
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env

# Ensure the environment variable is loaded
if "GOOGLE_API_KEY" not in os.environ:
    raise EnvironmentError("GOOGLE_API_KEY not found in environment variables.")


def get_few_shot_db_chain():
    MYSQL_DB_USER=os.environ.get("MYSQL_DB_USER")
    MYSQL_DB_PASSWORD=os.environ.get("MYSQL_DB_PASSWORD")
    MYSQL_DB_HOST=os.environ.get("MYSQL_DB_HOST")
    MYSQL_DB_NAME=os.environ.get("MYSQL_DB_NAME")
    db_user = MYSQL_DB_USER
    db_password = MYSQL_DB_PASSWORD
    db_host = MYSQL_DB_HOST
    db_name = MYSQL_DB_NAME

    # Connect to the database
    db_uri = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"
    db = SQLDatabase.from_uri(db_uri, sample_rows_in_table_info=3)

    # Initialize the language model
    google_api_key = os.environ.get("GOOGLE_API_KEY")
    llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=google_api_key, temperature=0.1)

    # Initialize embeddings and vectorstore
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    to_vectorize = [" ".join(example.values()) for example in few_shots]
    vectorstore = Chroma.from_texts(to_vectorize, embeddings, metadatas=few_shots)

    # Initialize example selector
    example_selector = SemanticSimilarityExampleSelector(
        vectorstore=vectorstore,
        k=2,
    )

    # Define the MySQL prompt
    mysql_prompt = """You are a MySQL expert. Given an input question, first create a syntactically correct MySQL query to run, then look at the results of the query and return the answer to the input question.
    Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per MySQL. You can order the results to return the most informative data in the database.
    Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
    Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
    Pay attention to use CURDATE() function to get the current date, if the question involves "today".

    Use the following format:

    Question: Question here
    SQLQuery: Query to run with no pre-amble
    SQLResult: Result of the SQLQuery
    Answer: Final answer here

    No pre-amble.
    """

    # Define the example prompt
    example_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult", "Answer"],
        template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
    )

    # Define the few-shot prompt template
    few_shot_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=mysql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["input", "table_info", "top_k"],  # These variables are used in the prefix and suffix
    )

    # Create the SQLDatabaseChain
    chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=few_shot_prompt)
    return chain

