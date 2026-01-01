from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles 
from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for simplicity; adjust as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate")
async def generate_post(request: Request):
    form = await request.form()

    role = form.get("role", "")
    role_other = form.get("role_other", "")
    tone = form.get("tone", "")
    purpose = form.get("purpose", "")
    highlight = form.get("highlight", "")
    insights = form.get("insights", "")
    gratitude = form.get("gratitude", "")
    tags = form.get("tags", "")
    resources = form.get("resources", "")
    date = form.get("date", "")
    reflection = form.get("reflection", "")
    cta = form.get("cta", "")
    hashtags = form.get("hashtags", "")
    extras = form.get("extras", "")
    print("Form data received:", form)
    final_role = role_other if role == "Other" and role_other else role

    

    # Build the prompt
    prompt = f"""
You are a professional LinkedIn content writer. Your task is to write an authentic, engaging, and well-structured LinkedIn post using the details below.

Start with a compelling **hook** – one sentence that grabs attention. It should be emotional, surprising, or thought-provoking (but not clickbait).

Main Post Inputs:
- Role: {final_role}
- Purpose: {purpose}
- Highlight or Announcement: {highlight}
- Tone: {tone}

Additional Context (include if relevant):
"""

    # Optional fields dictionary
    optional_fields = {
        "Key challenges or insights": insights,
        "People or groups to thank": gratitude,
        "Tagged individuals or companies": tags,
        "Relevant resources or links": resources,
        "Timeline or key dates": date,
        "Personal reflection or story": reflection,
        "Clear call-to-action": cta,
        "Relevant hashtags": hashtags,
        "Any additional notes": extras,
    }

    # Add optional fields to prompt
    for label, value in optional_fields.items():
        if value:
            prompt += f"- {label}: {value}\n"

    prompt += f"""
              Guidelines:
            - Write in short, skimmable paragraphs.
            - Use a {tone.lower()} tone – professional, but human and conversational.
            - Do **not** use emojis.
            - Avoid overused phrases like "excited to announce" or "game-changer."
            - Start with a hook line and end with a natural close or soft CTA (if applicable).
            - If the information provided is incomplete or vague:
            → Do NOT add fake details or assumptions.
            → Instead, either:
                a) Generate a short post using only the available details, OR
                b) Clearly respond that more context is needed to create a meaningful LinkedIn post.
            """

    print("Generated prompt:", prompt)

    # Call Groq API
    client = Groq(api_key=GROQ_API_KEY)
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1024,
        temperature=0.8,
    )

    print("API response received:", response)

    # Extract response
    linkedin_post = response.choices[0].message.content.strip()

    return {"linkedin_post": linkedin_post}
