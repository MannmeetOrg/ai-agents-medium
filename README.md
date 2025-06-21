
# 🧠 AI Blog Agent Pipeline

This project automates blog generation and publishing to [Medium.com](https://medium.com) using AI agents like OpenAI GPT and Gemini, SerpAPI, and browser automation with Selenium.

---

## 🚀 Features

- 🔍 Auto-selects topics from DevOps, AI, Microservices, Cloud.
- 🌐 Scrapes 10 real blog titles using SerpAPI.
- 🧠 Ranks titles using GPT-4 (fallback to Gemini API).
- 📝 Writes a 700-word blog in simple technical English.
- 🌍 Publishes automatically to Medium.com via Selenium.
- 🔐 Uses GitHub Secrets and CI/CD to automate publishing.

---

## 📁 Project Structure

```
.
├── .env                      # API keys and secrets (never commit this)
├── main.py                   # Entry point for the pipeline
├── blog_utils.py             # AI logic for topic, search, ranking, blog generation
├── selenium_publish.py       # Uses Selenium to automate Medium publishing
├── cookies.json              # Exported Medium login cookies (EditThisCookie)
├── requirements.txt          # Python dependencies
└── .github/workflows/publish.yml  # GitHub Actions CI/CD pipeline
```

---

## 🛠 Setup Instructions

### 1. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Create `.env` File

```env
OPENAI_API_KEY=your_openai_key
SERPAPI_KEY=your_serpapi_key
GEMINI_API_KEY=your_google_gemini_api_key
```

### 3. Export Medium Cookies

- Login to [Medium](https://medium.com)
- Use [EditThisCookie Chrome Extension](https://www.editthiscookie.com/)
- Export cookies and save as `cookies.json`

---

## ⚙️ GitHub Actions Integration

Set up `ENV_FILE` secret in your GitHub repository:

- Go to **Settings > Secrets > New Repository Secret**
- Name: `ENV_FILE`
- Paste the full `.env` content

Trigger the workflow manually or schedule it for automation.

---

## 🧪 To Run Locally

```bash
python main.py
```

---

## 🧠 Future Improvements

- Add content summarization or image generation
- Use LangChain for custom embeddings
- GUI-based blog customization

---

## 📃 License

This project is free and open for personal or educational use.
