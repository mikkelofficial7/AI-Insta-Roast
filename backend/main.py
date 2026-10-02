from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ollama import chat

app = FastAPI(title="Local Ollama API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RoastRequest(BaseModel):
    instagram_url: str


class RoastResponse(BaseModel):
    result: str


@app.post("/api/roast", response_model=RoastResponse)
async def roast_instagram(request: RoastRequest):
    prompt = f"""
    Roast this Instagram profile in Bahasa Indonesia with EXTREMELY funny, savage-but-playful humor, natural Indonesian slang, and high-level satire.

    Instagram:
    {request.instagram_url}

    Roasting style:
    - Make it VERY funny, absurd, witty, and entertaining.
    - Use natural Indonesian slang like how young Indonesians actually talk.
    - Use satire, exaggeration, irony, sarcasm, and clever punchlines.
    - Make it savage and slightly brutal, but clearly playful and comedic.
    - Make it feel like a close friend roasting someone in a group chat, not a formal critique.
    - Use unexpected comparisons, absurd observations, and creative punchlines.
    - Vary the jokes and sentence structures. Avoid repetitive roast patterns.
    - Only roast things that are actually visible or available from the profile.
    - Never invent facts about the person or their profile.
    - Do not make serious accusations or attack sensitive personal attributes.
    - Avoid discriminatory, hateful, or genuinely malicious insults.
    - Prioritize clever humor over simple name-calling.
    - Every section should have a strong comedic punchline.

    Output requirements:
    - Write the roast entirely in Bahasa Indonesia.
    - Use Markdown formatting.
    - Use **bold** for particularly funny punchlines or emphasis.
    - Do not explain that you are an AI.
    - Start roasting immediately.
    """

    response = chat(
        model="llama3.1:8b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return RoastResponse(
        result=response["message"]["content"]
    )