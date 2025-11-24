# Internship_Project_Smart_PCOD_Awareness_Chatbot

# 🌸 Smart PCOD Awareness Chatbot

A privacy-preserving, rule-based educational chatbot built with FastAPI + React + SQLite.

This interactive README guides you through the project structure, how to run it locally, how the rule engine works, and example interactions you can try. Use the collapsible sections to focus on the parts you need.

---

[TOC]
- Overview
- Purpose
- Quick Start
- Architecture & Workflow
- Backend: Structure & Details
- Frontend: Structure & Details
- Rules & Rule Engine
- Demo Scripts & Example Queries
- Development & Contribution
- License

---

## 🌟 Overview

The Smart PCOD Awareness Chatbot provides simple, evidence-informed education about PCOD (Polycystic Ovarian Disease). It is:

- Fully local (runs on your machine)
- Privacy-preserving (no user data is stored)
- Rule-based (keyword matching + priority)
- Designed for clear, non-judgmental replies suitable for diverse literacy levels

---

## 🎯 Purpose

- Improve public awareness of PCOD
- Provide consistent, structured answers
- Minimize misinformation with curated rule responses
- Demonstrate health informatics concepts (rule engines, data minimization)

---

## 🚀 Quick Start

<details>
<summary><strong>Prerequisites</strong> (expand)</summary>

- Python 3.9+
- Node.js 16+ and npm
- pip (Python package manager)
</details>

<details>
<summary><strong>Backend setup</strong></summary>

1. Create and activate a virtual environment (recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS / Linux
   venv\Scripts\activate      # Windows
   ```

2. Install Python dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. Seed the database (if provided as a script)

   ```bash
   python seed_data.py
   ```

4. Start the FastAPI server

   ```bash
   uvicorn main:app --reload
   ```

The backend serves a POST /chat endpoint that accepts JSON: { "message": "<user text>" } and returns a structured reply.
</details>

<details>
<summary><strong>Frontend setup</strong></summary>

1. From the frontend directory:

   ```bash
   npm install
   npm start
   ```

2. The React app (default) runs at http://localhost:3000 and calls the backend at http://127.0.0.1:8000/chat.

</details>

---

## 🧩 Architecture & Workflow

flowchart TD
A[User Types Message] --> B[React UI]
B --> C[Axios Sends Request]
C --> D[FastAPI Backend]
D --> E[Keyword Rule Engine]
E --> F[SQLite Rule Lookup]
F --> G[Return Educational Response]
G --> H[React Displays Reply]

Core components:
- React frontend: chat UI, message state, API calls
- FastAPI backend: API layer, rule engine, DB access
- SQLite + SQLAlchemy: stores rules (keyword → response → priority)
- Rule engine: cleans input, matches keywords, ranks by priority, returns best response

---

## 📁 Backend — Structure & Key Files

<details>
<summary><strong>chatbot.py — Rule Engine</strong></summary>

Purpose:
- Normalize and sanitize user input
- Tokenize input, check against stored rule keywords
- Apply priority ordering to select reply
- Return fallback message if nothing matches

Example function signature:

```python
def find_rule_reply(message: str, rules):
    # cleans message, splits words, matches keywords, returns best response
```

</details>

<details>
<summary><strong>database.py — DB configuration</strong></summary>

- Creates SQLAlchemy engine to SQLite
- Provides SessionLocal and declarative Base
- Configuration:

```python
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
```

</details>

<details>
<summary><strong>models.py — Rule model</strong></summary>

Example ORM model:

```python
class Rule(Base):
    __tablename__ = "rules"
    id = Column(Integer, primary_key=True, index=True)
    keywords = Column(String)   # comma-separated keyword list
    response = Column(String)
    priority = Column(Integer, default=0)
```

</details>

<details>
<summary><strong>seed_data.py — Seeder</strong></summary>

- Clears/initializes rule table
- Inserts curated PCOD awareness rules (symptoms, causes, myths, lifestyle tips)
- Run this to ensure you have baseline responses

</details>

<details>
<summary><strong>main.py — FastAPI app</strong></summary>

- Configures CORS
- Loads seeded data at startup (optional)
- Defines the /chat POST endpoint using Pydantic request/response models:

```python
@app.post("/chat")
def chat(request: ChatRequest):
    # call rule engine and return reply
```

</details>

---

## 🎨 Frontend — Structure & Key Files

<details>
<summary><strong>App.js</strong></summary>

- Mounts ChatBot component
- Provides any global providers or theme

</details>

<details>
<summary><strong>ChatBot.jsx</strong></summary>

- Manages messages list (user + bot)
- Sends user message with axios POST to /chat
- Receives and renders reply
- Auto-scrolls the message container
- Simple input bar with send button

Example API call:

```js
const res = await axios.post("http://127.0.0.1:8000/chat", { message: input });
```

</details>

<details>
<summary><strong>ChatBot.css</strong></summary>

- Styles: gradient background, rounded chat card, message bubbles
- Distinct colors for bot and user messages
- Mobile-friendly layout

</details>

---

## 🧠 Rules & Rule Engine — Design

- Rules are simple records mapping keywords (or keyword sets) to an educational response and a priority integer.
- Matching strategy:
  1. Lowercase and clean input (remove punctuation)
  2. Tokenize and match keywords (exact word match or simple substring)
  3. Collect all matching rules
  4. Sort matches by priority (higher priority wins)
  5. If multiple rules share top priority, combine or choose the most specific match
  6. Fallback message when no rules match

Example rule entry:

```json
{
  "keywords": "irregular periods,menstrual",
  "response": "Irregular periods can be a symptom of PCOD. It's helpful to track your cycle...",
  "priority": 10
}
```

Design notes:
- Keep rules evidence-based and non-judgmental.
- Use short, clear language. Offer next-step suggestions (track, consult clinician).
- Avoid giving medical diagnosis; this tool is educational only.

---

## 🎥 Demo Script & Example Queries

Use these prompts in the chat UI to demonstrate behavior.

<details>
<summary><strong>Start sequence</strong></summary>

- Start backend:
  uvicorn main:app --reload

- Start frontend:
  npm start

</details>

<details>
<summary><strong>Try these example user messages</strong></summary>

- "What are common PCOD symptoms?"
- "Why are my periods irregular?"
- "Can PCOD affect fertility?"
- "Is it just about weight?"
- "Diet tips for PCOD?"
- "Is PCOD the same as PCOS?"

Expect short educational replies and follow-up suggestions.
</details>

---

## ✅ Features

- Rule-based keyword matching
- Instant, local responses
- No storing of personal data
- Curated content covering symptoms, causes, cycles, fertility, diet & myths
- Modular and easy to extend

---

## 📂 Project File Tree (example)

<details>
<summary>Click to view</summary>

- backend/
  - main.py
  - chatbot.py
  - database.py
  - models.py
  - seed_data.py
  - requirements.txt
- frontend/
  - src/
    - App.js
    - ChatBot.jsx
    - index.js
    - ChatBot.css
- README.md

</details>

---

## 🛠 Development & Contribution

- To add or edit rules: update seed_data.py or interact with DB via SQLAlchemy session.
- Keep responses concise, evidence-based, and non-diagnostic.
- If you'd like to add localization or richer NLP, consider:
  - Storing synonyms per keyword
  - Adding a basic fuzzy match or stemming
  - Providing citations or "learn more" links (offline assets)

If you plan to contribute:
1. Fork the repo
2. Create a feature branch
3. Open a PR with a clear description of changes

---

## ⚖️ Disclaimer

This chatbot is educational only and not a substitute for professional medical advice. Encourage users with health concerns to consult a qualified clinician.

---

## 📄 License & Contact

- License: MIT (or project license)
- Maintainer: Project repository owner

---

If you'd like, I can:
- Generate example seed rules for common PCOD topics
- Create Postman examples or example curl requests for the /chat endpoint
- Convert the rules to a CSV or JSON for easier editing

Which of these would you like next?
