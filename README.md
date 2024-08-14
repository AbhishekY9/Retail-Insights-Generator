
# DreamWear T-Shirts: Database Q&A

This project leverages advanced language models and machine learning techniques to create a natural language interface for querying the DreamWear T-Shirts MySQL database. Store managers can ask questions about inventory, sales, and discounts in plain language, and the system will automatically generate and execute SQL queries to provide precise answers.




## Project Highlights

**Brands:** Van Heusen, Levi's, Nike, Adidas

**Database:** Inventory, sales, and discount information stored in MySQL

**Technologies:**

*Google Palm LLM:* For natural language understanding

*Hugging Face embeddings:* For embedding text queries
    
*LangChain framework:* For handling language models and query generation
    
*Chromadb:* As a vector store for efficient query processing
    
*Streamlit:* For creating a user-friendly web interface
    
*Few-shot learning:* To enhance the accuracy of the model with minimal examples
## Features

Natural Language Interface: Allows store managers to inquire about stock levels, sales projections, and more using plain language.

Automated SQL Generation: Translates natural language queries into SQL commands and retrieves accurate responses.

Real-time Interaction: Access the system via a web app and get instant answers.
## Usage


1. Clone the repository:

    git clone https://github.com/your-username/dreamwear-tshirts-qa.git

2. Navigate to the project directory:

    cd dreamwear-tshirts-qa

3. Install the required Python packages:

    pip install -r requirements.txt

4. Set up your environment variables by creating a .env file and adding your Google API key:


    GOOGLE_API_KEY=your_google_api_key_here

5. Launch the Streamlit app:

    streamlit run main.py

6. Open your browser and start asking questions about your inventory, sales, and more.
## Sample Questions

* How many t-shirts do we have left in stock in total?

* How many extra-small, white t-shirts do we have from Nike?

* What is the total inventory value for all medium-sized t-shirts?

* How much revenue can we generate if we sell all small-sized Adidas t-shirts today after discounts?
## Project Structure

* main.py: The primary Streamlit application script.

* langchain_helper.py: Contains all LangChain-related code.

* requirements.txt: List of Python packages required for the project.

* few_shots.py: Includes few-shot prompts for the LLM.

* .env: Configuration file for storing your Google API key.
## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

