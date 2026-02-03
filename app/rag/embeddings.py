from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from app.config import settings
import os

VECTOR_DB_PATH = "app/vectorstore"


class VectorStore:
    def __init__(self, documents: list[str], sources: list[str]):
        self.embedding_model = GoogleGenerativeAIEmbeddings(
            model=settings.EMBEDDING_MODEL,google_api_key=settings.GOOGLE_API_KEY)
        index_file = os.path.join(VECTOR_DB_PATH, "index.faiss")
        metadatas = [{"source": src} for src in sources]

        if os.path.exists(index_file):
            self.db = FAISS.load_local(
                VECTOR_DB_PATH,
                self.embedding_model,
                allow_dangerous_deserialization=True
            )
        else:
            self.db = FAISS.from_texts(documents, self.embedding_model, metadatas=metadatas)
            os.makedirs(VECTOR_DB_PATH, exist_ok=True)
            self.db.save_local(VECTOR_DB_PATH)
            print("Vector store saved.")
    def search(self, query: str, k: int = 3):
        docs = self.db.similarity_search(query, k=k)
        return docs
