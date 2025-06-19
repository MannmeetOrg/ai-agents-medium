# README.md

## 🤖 AI Blog Agent with Gemini Pro & Medium Automation

Automatically generate and publish blog articles on Medium using AI-generated content with Gemini Pro, topic ideas from Google Search, and Selenium automation.

---

## 🚀 Features
- 🔍 Automatically select trending tech topics (DevOps, AI, Cloud, Microservices)
- 🤖 Uses **Gemini Pro** (Google Generative AI) for idea refinement and blog generation
- 🌐 Uses **SerpAPI** to search for blog ideas
- ✍️ Publishes blogs to your **Medium.com** account using Selenium (headless browser)
- 🛠️ Integrated with **GitHub Actions** to run as a CI/CD automation pipeline

---

## 🧩 Technologies Used
- [Gemini Pro API](https://makersuite.google.com/app/apikey)
- [SerpAPI](https://serpapi.com)
- [Selenium](https://selenium.dev)
- GitHub Actions

---

## 📁 Project Structure
```
├── .env.example              # Environment variables template
├── main.py                   # Pipeline entrypoint
├── blog_utils.py             # Gemini Pro logic for content generation
├── selenium_publish.py       # Medium.com publishing automation
├── requirements.txt          # Python dependencies
└── .github/workflows/publish.yml  # GitHub Actions pipeline
```

---

## 🔧 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/ai-blog-agent.git
cd ai-blog-agent
```

### 2️⃣ Create `.env` File
Copy the example and fill in your credentials:
```bash
cp .env.example .env
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up GitHub Secrets
Go to your repo → **Settings → Secrets → Actions** → Add the following:
- `GEMINI_API_KEY`
- `SERPAPI_KEY`
- `MEDIUM_USERNAME`
- `MEDIUM_PASSWORD`

### 5️⃣ Run Locally (Headless)
```bash
xvfb-run python main.py
```

### 6️⃣ Trigger via GitHub Action
Go to **Actions tab** → Run the `Publish Blog to Medium (Gemini)` workflow manually.

---

## 📌 Notes
- Make sure your Medium account supports login via email/password (not SSO).
- Gemini Pro offers **60 free API calls/day** — enough for blog generation.
- SerpAPI requires a free or paid key — sign up at [serpapi.com](https://serpapi.com)

---

## 📮 Output Example
```
Chosen topic: Cloud
Ideas fetched: [...]
Top 5 topics: [...]
✅ Blog published successfully.
```

---

## 📜 License
MIT License. Feel free to fork and build your AI blogging army!

---

## 🙋‍♀️ Created by
**@manmeet.ai** — For learning, AI automation, and DevOps ❤️
