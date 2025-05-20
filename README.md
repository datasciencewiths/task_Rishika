# 🧠 AI-Powered Prompt Engineering Microservice with Streamlit UI

## ✨ Project Overview

This project is built as part of an AI Internship Assessment. It is a full-stack AI-powered web prototype that:

- Accepts user input via a clean **Streamlit UI**
- Generates two types of AI responses:
  - A **casual/creative** tone
  - A **formal/analytical** tone
- Saves every interaction in a **PostgreSQL** database
- Uses a **FastAPI** backend microservice to handle request processing and persistence
- Supports prompt engineering and response refinement using **OpenAI GPT models**

---

## 🚀 Features

- 🎨 Dual-tone AI prompt engineering (casual vs formal)
- 🔌 FastAPI backend with robust REST endpoints
- 💾 PostgreSQL data persistence with timestamp & user ID tracking
- 📊 Streamlit frontend to display results + past queries
- 🧪 Modular code with unit test hooks (mock-friendly)
- ⚙️ `.env` support for API keys and DB credentials
- ✅ One-click deployable to Render or Streamlit Cloud
- 🧱 Clean, extendable architecture (backend/frontend separation)

---

## 🧱 Architecture

User ↔ Streamlit UI ↔ FastAPI Backend ↔ PostgreSQL Database
↕
OpenAI API

yaml
Copy
Edit

- **Frontend:** Streamlit  
- **Backend:** FastAPI  
- **Database:** PostgreSQL  
- **LLM:** OpenAI GPT-3.5/4 (can mock or use Hugging Face models)  
- **Testing:** Pytest-ready stubs (prompt logic, routes)

---

## 🧠 Prompt Engineering Strategy

### Styles Implemented:
1. **Casual/Creative Style**
   - Fun, friendly, conversational tone
   - Example prompt:  
     ```
     Explain the topic of {query} like you're chatting with a friend over coffee.
     ```
2. **Formal/Analytical Style**
   - Academic, structured explanation
   - Example prompt:  
     ```
     Provide a formal, well-reasoned explanation of {query} as if writing an academic paper.
     ```

💡 _Bonus Tip:_ This structure can be extended with **prompt chaining** (generate → polish → summarize).

---

## 📂 Project Structure

├── app/
│ ├── main.py # FastAPI app with endpoints
│ ├── models.py # SQLAlchemy DB models
│ ├── database.py # PostgreSQL engine & session
│ ├── prompt_engineering.py # Core AI logic
│ └── utils.py # UUID, timestamp helpers
│
├── streamlit_app.py # Streamlit frontend app
├── requirements.txt # Python dependencies
├── .env.example # Example environment variables
├── README.md # This file
└── tests/
├── test_prompt_logic.py
└── test_api_routes.py

yaml
Copy
Edit

---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/ai-intern-assessment.git
cd ai-intern-assessment
2. Setup Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate (Windows)
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Configure .env File
Create a .env file using .env.example:

env
Copy
Edit
OPENAI_API_KEY=your_openai_key
DATABASE_URL=postgresql://user:password@localhost/dbname
5. Run FastAPI Backend
bash
Copy
Edit
uvicorn app.main:app --reload
6. Run Streamlit Frontend
bash
Copy
Edit
streamlit run streamlit_app.py
🧪 Testing
Run Unit Tests
bash
Copy
Edit
pytest tests/
test_prompt_logic.py — tests formatting + mock model outputs

test_api_routes.py — endpoint response validation

🖥️ API Documentation
POST /generate
json
Copy
Edit
Request:
{
  "user_id": "abc123",
  "query": "What is blockchain?"
}
json
Copy
Edit
Response:
{
  "casual_response": "...",
  "formal_response": "..."
}
GET /history?user_id=abc123
json
Copy
Edit
[
  {
    "query": "What is blockchain?",
    "casual_response": "...",
    "formal_response": "...",
    "timestamp": "2025-05-20T12:34:56"
  },
  ...
]
📦 Deployment Options
✅ Streamlit Cloud (Frontend Only)
Push repo to GitHub

Deploy at streamlit.io/cloud

Set secrets in app settings (OPENAI_API_KEY, BACKEND_URL)

✅ Render.com (Full Stack)
Deploy both FastAPI and Streamlit as separate services

Use Render’s free PostgreSQL add-on or connect external DB

Add environment variables via dashboard

🧱 Future Improvements (Optional Ideas)
Hugging Face fallback model (offline support)

Prompt chaining or multi-turn memory

User auth (JWT or mock)

Docker + CI pipeline

Chat-style threaded UI

🧾 License
MIT License — use it freely, customize for your own projects or hiring assessments.

🙌 Credits
Developed by [Your Name]
AI + Full Stack Developer Intern Candidate
Tech Stack: OpenAI, FastAPI, Streamlit, PostgreSQL, Python

yaml
Copy
Edit

---

Let me know if you'd like:

- A **Dockerized version**
- This published on **GitHub** with proper structure
- Or help converting it into a **hosted live demo**

Ready when you are!
