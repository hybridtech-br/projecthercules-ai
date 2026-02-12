from fastapi import FastAPI, Request
from wake_phrases import get_wake_phrases

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Project Hercules AI is running"}

@app.post("/ask")
async def ask(request: Request):
    payload = await request.json()
    user_input = payload.get("message", "").lower()

    accept_language = request.headers.get("accept-language", "en")
    lang_code = accept_language.split(",")[0][:2]

    wake_phrases = get_wake_phrases(lang_code)

    if not any(user_input.startswith(phrase) for phrase in wake_phrases):
        return {
            "response": "Wake phrase not detected.",
            "expected": wake_phrases
        }

    for phrase in wake_phrases:
        if user_input.startswith(phrase):
            user_input = user_input.replace(phrase, "").strip()

    responses = {
        "en": f"I am listening. You said: {user_input}",
        "pt": f"Estou ouvindo. Você disse: {user_input}",
        "es": f"Estoy escuchando. Dijiste: {user_input}",
        "fr": f"Je vous écoute. Vous avez dit: {user_input}",
        "de": f"Ich höre zu. Du hast gesagt: {user_input}"
    }

    return {"response": responses.get(lang_code, responses["en"])}
