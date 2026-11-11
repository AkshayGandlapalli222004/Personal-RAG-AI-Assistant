from src.rag.data_loader import load_all_documents
from src.rag.embedding import EmbeddingsPipeline
from src.rag.vectorstore import FaissVectorStore
from src.rag.search import RAGSearch


#Example Usage through a pipelinef


if __name__ == "__main__":
    docs  = load_all_documents("data")
    store = FaissVectorStore("faiss_store")
    store.build_from_documents(docs)

    store.load()

    #print(store.query("What is the Attention Mechanism?", top_k = 4))
    rag_search = RAGSearch()
    query = "What is the so called Attention Mechanism in LLM"
    summary = rag_search.search_and_summarise(query, top_k = 4)

    print("Summary:", summary)


    #print(chunkvectors)