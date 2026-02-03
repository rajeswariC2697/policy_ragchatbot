from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from app.config import settings
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
class AnswerGenerator:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model=settings.LLM_MODEL, google_api_key=settings.GOOGLE_API_KEY, temperature=0, max_tokens=300)

        self.prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="""
                You are a Company HR Policy Assistant.

                Your task is to answer questions ONLY using the provided policy context.

                If the user message is a greeting such as:
                "hi", "hello", "hey", "good morning", "good evening"

                Respond politely with a greeting and ask how you can help with company policies.

                Example:
                "Hello! How can I assist you with company policies today?"

                Do NOT provide policy information in greeting responses.

                STRICT RULES (NO EXCEPTIONS):

                1. Use ONLY the information present in the CONTEXT section.
                2. DO NOT use prior knowledge, assumptions, or general HR practices.
                3. If the answer is not clearly found in the context, you MUST respond EXACTLY with:
                    "Please ask a question related to the policies."

                4. Do not guess.
                5. Do not summarize beyond the context.
                6. Do not add advice, opinions, or external information.

                When answering:
                - Be clear and concise.
                - Quote or paraphrase only what is supported by the context.

                CONTEXT:
                {context}

                QUESTION:
                {question}

                FINAL ANSWER:

                """
        )

    def generate(self, question: str, context: str) -> str:
        formatted_prompt = self.prompt.format(context=context, question=question)
        response = self.llm.invoke(formatted_prompt)
        return response.content.strip()
