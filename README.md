****************DreamWear T-Shirts: Database Q&A****************

This project leverages Google Palm and Langchain to create a system capable of interacting with a MySQL database through natural language queries. At DreamWear T-Shirts, we manage our inventory, sales, and discount information in a MySQL database. Store managers can inquire about stock levels, potential sales, and more in plain language, and the system will translate these questions into SQL queries and provide accurate responses.

**Project Highlights**

DreamWear T-Shirts offers a variety of brands including Van Heusen, Levi's, Nike, and Adidas.
Our inventory, sales, and discount information is maintained in a MySQL database.
We are developing an LLM-powered Q&A system using:

Google Palm LLM

Hugging Face embeddings

Streamlit for the user interface

Langchain framework

Chromadb as a vector store

Few-shot learning

The user interface will allow store managers to ask questions in natural language and receive precise answers.

**Usage**

Launch the Streamlit app by running streamlit run main.py.

Access the web app in your browser and start asking questions.

**Sample Questions**

How many t-shirts do we have left in stock in total?

How many extra-small, white t-shirts do we have from Nike?

What is the total inventory value for all medium-sized t-shirts?

How much revenue can we generate if we sell all small-sized Adidas t-shirts today after discounts?

**Project Structure**

main.py: The primary Streamlit application script.

langchain_helper.py: Contains all the Langchain-related code.

requirements.txt: A list of Python packages required for the project.

few_shots.py: Includes few-shot prompts for the LLM.

.env: Configuration file for storing your Google API key.