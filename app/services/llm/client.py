from groq import Groq
from app.config import settings

client = Groq(api_key=settings.GROQ_API_KEY)


def call_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",   # ✅ free + fast
        messages=[
            {"role": "system", "content": "You are a cloud infrastructure expert."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
        max_tokens=400,
    )

    return response.choices[0].message.content
