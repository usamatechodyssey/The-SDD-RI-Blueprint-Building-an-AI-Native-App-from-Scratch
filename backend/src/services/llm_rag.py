#backend/src/services/llm_rag.py

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.documents import Document
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import Qdrant
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from backend.src.services.qdrant import get_qdrant_client

OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY"
)  # Assuming OPENAI_API_KEY is used for Gemini via Claude Router

# Initialize LLM (Gemini Flash via Claude Router)
llm = ChatGoogleGenerativeAI(model="gemini-flash", google_api_key=OPENAI_API_KEY)

# Initialize Qdrant client for embeddings
qdrant_client = get_qdrant_client()
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001", google_api_key=OPENAI_API_KEY
)

# Define a dummy collection name for now; this should be dynamic
COLLECTION_NAME = "my_rag_collection"

# Placeholder for vector store, will be properly initialized later
vector_store = Qdrant(client=qdrant_client, collection_name=COLLECTION_NAME, embeddings=embeddings)

# Prompt template for RAG
prompt = ChatPromptTemplate.from_template(
    """Answer the following question based only on the provided context:
    <context>
    {context}
    </context>
    Question: {input}"""
)

# Document chain for combining documents
document_chain = create_stuff_documents_chain(llm, prompt)

# Retrieval chain for RAG
retrieval_chain = create_retrieval_chain(vector_store.as_retriever(), document_chain)


def get_rag_chain():
    """Returns the configured RAG chain."""
    return retrieval_chain


# Example usage (for testing, not part of API)
if __name__ == "__main__":
    # This part would typically be used in an API endpoint
    # For demonstration, let's assume we have some documents
    docs = [
        Document(
            page_content="LangChain is a framework for developing applications powered by language models."
        ),
        Document(
            page_content="Qdrant is a vector database for high-performance similarity search."
        ),
    ]
    # In a real scenario, you would add these documents to the vector store
    # For now, we'll simulate retrieval

    # You would typically pass actual context from a retriever here
    # For this example, we'll just demonstrate the chain structure
    # result = retrieval_chain.invoke({"input": "What is LangChain?", "context": docs})
    # print(result)
    print("RAG chain initialized. This is a placeholder for actual RAG execution.")
