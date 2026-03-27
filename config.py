import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

def get_llm():
    return LLM(
        model="groq/llama-3.3-70b-versatile",   # ✅ CrewAI format: provider/model
        api_key=os.getenv("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"),
        temperature=0.3,
        max_tokens=4096
    )