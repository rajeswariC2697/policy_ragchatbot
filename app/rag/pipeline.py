from app.rag.loader import load_policies
from app.rag.embeddings import VectorStore
from app.rag.generator import AnswerGenerator
from app.models.schemas import AnswerResponse

class RAGPipeline:
    def __init__(self):
        self.documents, self.sources = load_policies()
        self.vector_store = VectorStore(self.documents, self.sources)
        self.generator = AnswerGenerator()

    def answer(self, question: str) -> AnswerResponse:
        docs = self.vector_store.search(question)

        context_blocks = [doc.page_content for doc in docs]
        context = "\n\n".join(context_blocks)

        answer = self.generator.generate(question, context)

        return AnswerResponse(answer=answer, sources=[doc.metadata.get("source", "policy") for doc in docs])

rag_pipeline = RAGPipeline()
