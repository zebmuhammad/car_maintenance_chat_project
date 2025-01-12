import pandas as pd
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
import os
import shutil
from dotenv import load_dotenv

load_dotenv()

def loader(file_path):
    try:
        print("Starting loader function...")  # Debug
        # Initialize OpenAI embeddings
        embeddings = OpenAIEmbeddings()

        # Clear previous Chroma database
        if os.path.exists("./chromadb"):
            shutil.rmtree("./chromadb")
            print("Cleared previous Chroma database.")  # Debug

        # Initialize Chroma vectorstore
        vectorstore = Chroma(
            persist_directory="./chromadb",
            embedding_function=embeddings,
            collection_name="car_maintenance"
        )
        print("Initialized Chroma vectorstore.")  # Debug

        # Load CSV data
        df = pd.read_csv(file_path)
        print("Loaded CSV data.")  # Debug

        # Debug: Print the first few rows of the DataFrame
        print("DataFrame head:\n", df.head())

        # Fill NaN values with an empty string
        df.fillna('', inplace=True)

        # Combine relevant columns into a single text field
        df["combined"] = (
            "Issue: " + df["Issue"].astype(str) + "\n" +
            "Symptoms: " + df["Symptoms"].astype(str) + "\n" +
            "Causes: " + df["Causes"].astype(str) + "\n" +
            "Solutions: " + df["Solutions"].astype(str)
        )

        # Prepare the data for embeddings
        text_data = df["combined"].tolist()

        # Debug: Print the combined text data
        print("Combined text data:", text_data)

        # Split texts into smaller chunks
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

        # Ensure all entries are strings and filter out any non-string types
        chunks = []
        for text in text_data:
            if isinstance(text, str):  # Check if the text is a string
                chunks.extend(text_splitter.split_text(text))
            else:
                print(f"Warning: Skipping non-string entry: {text}")

        # Debug: Print the number of chunks created
        print(f"Number of chunks created: {len(chunks)}")

        # Add texts to the vectorstore
        vectorstore.add_texts(texts=chunks)
        print(f"Added {len(chunks)} chunks to the vectorstore.")

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
    except Exception as e:
        print(f"An error occurred: {e}")

def retriever(question: str):
    try:
        print("Starting retriever function...")  # Debug
        embeddings = OpenAIEmbeddings()

        # Load Chroma vectorstore
        vectorstore = Chroma(
            persist_directory="./chromadb",
            embedding_function=embeddings,
            collection_name="car_maintenance"
        )
        print("Loaded Chroma vectorstore.")  # Debug

        # Perform similarity search
        results = vectorstore.similarity_search(question, k=4)
        print("Similarity search results:", results)  # Debug
        return [result.page_content for result in results]

    except Exception as e:
        print(f"An error occurred during retrieval: {e}")
        return []

# Example usage
file_path = "updated_car_maintenance_issues.csv"  
if os.path.exists(file_path):
    print("CSV file found.")  # Debug
    loader(file_path)

    question = "What are the common causes of engine overheating?"
    docs = retriever(question)
    print("Retrieved Documents:")
    for doc in docs:
        print(doc)
else:
    print(f"File not found: {os.path.abspath(file_path)}")
