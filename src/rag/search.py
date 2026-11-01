# Integrating LLM

import os
from dotenv import load_dotenv
from src.rag.vectorstore import FaissVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

class RAGSearch:

    def __init__(self, persist_dir: str = "faiss_store", embedding_model: str = "all-MiniLM-L6-v2"):
        self.vectorstore = FaissVectorStore(persist_dir, embedding_model)

        #Loading or Building Vector Store

        faiss_path = os.path.join(persist_dir, "faiss.index")
        meta_path = os.path.join(persist_dir, "metadata.pkl")


        if not(os.path.exists(faiss_path) and os.path.exists(meta_path)):
            from src.rag.data_loader import load_all_documents
            docs = load_all_documents("data")
            self.vectorstore.build_from_documents(docs)
        else:
            self.vectorstore.load()

        model_name = "gemma-4-26b-a4b-it"
        google_api_key = os.getenv("Google_Api_Key")
        self.llm = ChatGoogleGenerativeAI(google_api_key = google_api_key, model = model_name , temperature = 0.1, max_tokens = 1024)
        print(f"[INFO] Google Gemini Intialised:{model_name}")


    def search_and_summarise(self, query: str, top_k: int = 5) -> str:
        results = self.vectorstore.query(query, top_k = top_k)
        texts = [r["metadata"].get("text","") for r in results if r["metadata"]]
        context = "\n\n".join(texts)

        if not context:
            return "No Relevant Context Found"
        prompt = f"""Sumarize the following context for the Query: '{query}' \n\n Context: \n\n Getting up with the context:"""

        response = self.llm.invoke([prompt])
        return response.content

