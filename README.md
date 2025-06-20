# README.md

## 🤖 AI Blog Agent with Gemini Flash & Medium Automation

Automatically generate and publish blog articles on Medium using AI-generated content with **Gemini Flash** (fallback to Pro 2.5), topic ideas from Google Search, and Selenium automation.

---

## 🚀 Features
- 🔍 Automatically select trending tech topics (DevOps, AI, Cloud, Microservices)
- 🤖 Uses **Gemini Flash** (fallback to **Pro 2.5**) for idea refinement and blog generation
- 🌐 Uses **SerpAPI** to search for blog ideas
- ✍️ Publishes blogs to your **Medium.com** account using Selenium and saved cookies
- 🛠️ Integrated with **GitHub Actions** to run as a CI/CD automation pipeline

---

## 🧩 Technologies Used
- [Gemini API (Flash or Pro 2.5)](https://makersuite.google.com/app/apikey)
- [SerpAPI](https://serpapi.com)
- [Selenium](https://selenium.dev)
- GitHub Actions

---

## 📁 Project Structure
```
├── .env                      # API keys for Gemini & SerpAPI
├── main.py                   # Pipeline entrypoint
├── blog_utils.py             # Gemini logic with fallback support
├── selenium_publish.py       # Medium.com publishing automation using cookies.json
├── cookies.json              # Exported cookies for Medium login
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
```bash
cp .env.example .env
```
Add your credentials to `.env`:
```
GEMINI_API_KEY=your_key_here
SERPAPI_KEY=your_serpapi_key_here
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up GitHub Secrets (Optional for CI)
In your GitHub repo → **Settings → Secrets → Actions**:
- `GEMINI_API_KEY`
- `SERPAPI_KEY`

### 5️⃣ Export Cookies from Medium
1. Open [https://medium.com](https://medium.com) and login.
2. Use [EditThisCookie](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg) to export cookies.
3. Save the exported cookies as `cookies.json` in your project root.

### 6️⃣ Run Locally (Headless)
```bash
xvfb-run python main.py
```

### 7️⃣ Trigger via GitHub Action
Use **Actions** tab → `Publish Blog to Medium (Gemini)` workflow.

---

## 📌 Notes
- Cookie-based login is used due to Medium's restriction on automation
- Gemini Flash is fast and economical; Pro 2.5 fallback ensures reliability
- SerpAPI provides structured blog search results

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
MIT License. Fork freely and start your blog automation!

---

## 🙋‍♀️ Created by
**@manmeet.ai** — AI, DevOps & Content Automation ❤️
