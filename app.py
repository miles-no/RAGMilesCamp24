import os
from openai import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
import numpy as np
from dotenv import load_dotenv
load_dotenv()
# Initialize OpenAI client
client = OpenAI()

# Main RAG pipeline
def rag_pipeline(directory_path, user_query):
    documents = load_documents(directory_path)
    embeddings = embed_documents(documents)
    relevant_docs = retrieve_relevant_docs(documents, embeddings, user_query)
    generated_answer = generate_answer(relevant_docs, user_query)
    return generated_answer

def load_documents(directory_path):
    documents = []
    # Loop through all files in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if filename.endswith(".txt"):
            loader = TextLoader(file_path)
            doc = loader.load()
            documents.extend(doc)  # Add each document to the list
    return documents

def embed_documents(documents):
    embeddings = []
    for doc in documents:
        response = client.embeddings.create(
            model="text-embedding-3-large",  # Example from OpenAI docs, modify if needed
            input=doc.page_content
        )
        # Access the embedding from the response object correctly
        embeddings.append(np.array(response.data[0].embedding))  # Use .data and .embedding
    return embeddings

def retrieve_relevant_docs(documents, embeddings, query):
    # Embed the user query using OpenAI
    response = client.embeddings.create(
        model="text-embedding-3-large",  # Use the same embedding model for the query
        input=query
    )
    # Access the embedding from the response object correctly
    query_embedding = np.array(response.data[0].embedding)
    
    # Calculate cosine similarity between query embedding and document embeddings
    similarities = [np.dot(query_embedding, emb) / (np.linalg.norm(query_embedding) * np.linalg.norm(emb)) for emb in embeddings]
    
    # Get top 5 most similar documents (or fewer if there aren't enough)
    top_doc_indices = np.argsort(similarities)[-3:][::-1]  # Get indices of top 5 most similar documents
    relevant_docs = [documents[i] for i in top_doc_indices]
    
    return relevant_docs


def generate_answer(relevant_docs, query):
    context = " ".join([doc.page_content for doc in relevant_docs])
    # Using OpenAI's chat completion API
    completion = client.chat.completions.create(
        model="gpt-4o-mini",  # Modify this to the desired GPT-4 model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Based on the following context, answer this question: {query}\n\nContext: {context}"}
        ]
    )
    return completion.choices[0].message.content.strip()

if __name__ == "__main__":
    # Directory path is set to 'data', which is in the same folder as the script
    directory_path = "./data"
    
    user_query = input("Enter your query: ")
    
    response = rag_pipeline(directory_path, user_query)
    print(f"\nAnswer: {response}")
