# GenAI Backend Kit

A production-style backend boilerplate to build powerful Generative AI applications using FastAPI, Groq API, LangChain, and other modern tools. This project provides a clean, modular structure with API key authentication, configuration management, logging, and route handling.

---

## 🚀 Features

- ✨ FastAPI-based modular backend
- 🔐 API key-based request authentication
- 🧠 Integrate any LLM (e.g., Groq's LLaMA3) easily
- 🪵 Production-grade logging
- 🔧 Clean config management via JSON and `pydantic`
- 📁 Environment-based settings
- 🧪 Easy to test & extend

---

## 📁 Folder Structure

```
.
├── app/
│   ├── __init__.py
│   ├── config.py               # Loads .env and config.json
│   ├── logger.py               # Rotating log setup
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       └── health.py       # GET /health
│   ├── services/
│   │   └── __init__.py     # Handles business logic
│   └── llm/
│       └── groq_llm.py         # Groq API integration
├── .env                        # Environment-specific secrets
├── config.json                 # Static app configuration
├── main.py                     # FastAPI entry point
├── requirements.txt
└── logs/
    └── app.log                 # Auto-created log file

```

---

## 🧪 Setup & Run

### 1. Clone & Setup
```bash
git clone https://github.com/siddhardhan23/genai-backend-kit.git
cd genai-backend-kit
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Add Environment Variables
Create a `.env` file or use `config/dev.env`:
```
GROQ_API_KEY=your_groq_api_key
APP_API_KEY=your_custom_api_key
```

### 3. Run FastAPI App
```bash
uvicorn main:app --reload
```

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for Swagger UI.

---

## 🔐 API Key Auth
All routes (except `/health`) require a valid `x-api-key` header.

```http
GET /ask
x-api-key: your_custom_api_key
```

---

## 📡 Example Endpoint: `/ask`

```http
POST /ask
{
  "query": "Explain what is LangChain."
}
```
Returns the response from Groq LLM via `groq_service.py`.

---

## 🛠 Built With
- [FastAPI](https://fastapi.tiangolo.com/)
- [Groq](https://groq.com/) LLaMA 3 Models
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/)
- Python Logging

---

---

## 📄 License
[MIT](LICENSE)

---

## 🙌 Author
[Siddhardhan](https://github.com/siddhardhan23)

## YouTube
[Siddhardhan](https://www.youtube.com/channel/UCG04dVOTmbRYPY1wvshBVDQ)

