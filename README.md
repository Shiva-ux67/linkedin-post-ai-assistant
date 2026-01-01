🤖 AI LinkedIn Post Generator

An intelligent content creation tool built with Python and FastAPI. This application leverages the Groq Cloud API (Llama 3) to transform user inputs into professional, engaging, and high-conversion LinkedIn posts.
✨ Key Features

    AI-Powered Generation: Uses the high-speed llama3-8b-8192 model via Groq.

    Customizable Personas: Tailors content based on roles like Student, Engineer, or Manager.

    Tone Control: Choose between Professional, Conversational, or Friendly tones.

    Smart Hooks: Automatically generates attention-grabbing opening lines.

    FastAPI Backend: Built for speed and efficiency with asynchronous processing.

    Clean UI: Simple, responsive frontend using Jinja2 templates and CSS.

🛠️ Tech Stack

    Backend: Python, FastAPI

    AI Engine: Groq SDK (Llama 3 Model)

    Frontend: HTML5, CSS3, Jinja2 Templates

    Environment: Python-dotenv (Security)

🚀 Getting Started
1. Clone the Repository
Bash

git clone https://github.com/Shiva-ux67/linkedin-post-ai-assistant.git
cd linkedin-post-ai-assistant

2. Set Up Environment Variables

Create a .env file in the root directory and add your API key:
Plaintext

GROQ_API_KEY=your_actual_api_key_here

3. Install Dependencies
Bash

pip install -r requirements.txt

4. Run the Application
Bash

uvicorn main:app --reload

Open your browser and navigate to http://127.0.0.1:8000.
📂 Project Structure
Plaintext

├── main.py          # FastAPI application logic
├── .env             # API keys (Ignored by Git)
├── .gitignore       # Files to exclude from GitHub
├── requirements.txt # Project dependencies
├── static/          # CSS and static assets
└── templates/       # HTML files (index.html)

🛡️ License

This project is open-source and available under the MIT License.
