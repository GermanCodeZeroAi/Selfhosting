from fastapi import FastAPI
from pydantic import BaseModel
import os, httpx
OLLAMA = os.getenv("OLLAMA_HOST","http://host.docker.internal:11434")
MODEL = os.getenv("OLLAMA_MODEL","llama3.2:3b-instruct")
app = FastAPI(title="GCZA Drafting Service")

class DraftReq(BaseModel):
    subject: str
    body_preview: str
    intent: str
    style: str = "freundlich, präzise, kurz"

@app.post("/draft")
async def draft(req: DraftReq):
    sys_prompt = f"Du schreibst deutsche E-Mails. Intent={req.intent}. Stil={req.style}. Antworte nur mit dem finalen Text."
    user = f"Betreff: {req.subject}\nAuszug:\n{req.body_preview}\n— Bitte formuliere eine passende Antwort."
    payload = {"model": MODEL, "prompt": f"{sys_prompt}\n\n{user}", "stream": False}
    async with httpx.AsyncClient(timeout=120) as cx:
        r = await cx.post(f"{OLLAMA}/api/generate", json=payload)
        r.raise_for_status()
        txt = r.json().get("response","")
    return {"draft": txt.strip()}