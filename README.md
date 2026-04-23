# 🏏 IPL Score — Live Cricket Web App

<p align="center">
  <a href="https://ipl-score-dx4s.onrender.com/static/index.html">
    <img src="https://img.shields.io/badge/Live-Demo-00c853?style=for-the-badge&logo=render&logoColor=white" />
  </a>
  <a href="https://github.com/Anant-083/ipl_score">
    <img src="https://img.shields.io/badge/GitHub-Repo-181717?style=for-the-badge&logo=github" />
  </a>
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/FastAPI-0.100+-green?style=for-the-badge&logo=fastapi" />
</p>

---

## ✨ Overview

A minimal, real-time IPL scorecard web app built using **FastAPI** and the **Cricbuzz API**. Shows live IPL scores, upcoming fixtures, and the full points table — all updated automatically every 5 minutes.

---

## 🚀 Live Demo

**👉 [https://ipl-score-dx4s.onrender.com/static/index.html](https://ipl-score-dx4s.onrender.com/static/index.html)**

> ⚠️ Hosted on Render free tier — may take 30–50 seconds to wake up on first visit.

---

## 🎯 Features

- 🔴 Live IPL match scores
- 📅 Upcoming IPL fixtures (shown when nothing is live)
- 📊 Points table with NRR and playoff zone highlighted
- ⚡ Auto-refresh every 5 minutes
- 🎨 Team color badges for all 10 IPL teams
- 📱 Responsive — works on mobile and desktop
- 🌙 Minimal dark UI

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI, Python 3.11, httpx |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Data Source | Cricbuzz API via RapidAPI |
| Deployment | Render (Free Tier) |

---

## 📁 Project Structure
ipl_score/
├── frontend/
│   ├── index.html       # Main UI
│   ├── style.css        # Dark theme styles
│   └── app.js           # Fetch + render logic
├── engine.py            # Cricbuzz API integration
├── main.py              # FastAPI routes
├── requirements.txt     # Python dependencies
└── .env                 # API keys 
---

## ⚙️ Setup Locally

**1. Clone the repository**
```bash
git clone https://github.com/Anant-083/ipl_score.git
cd ipl_score
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Create `.env` file**
API_TOKEN=your_rapidapi_key_here
API_HOST=cricbuzz-cricket.p.rapidapi.com

> Get your free API key at [RapidAPI — Cricbuzz Cricket](https://rapidapi.com/cricbuzz/api/cricbuzz-cricket)

**4. Run the server**
```bash
uvicorn main:app --reload
```

**5. Open in browser**
http://localhost:8000/static/index.html

---

## ☁️ Deployment on Render

1. Push code to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Connect your GitHub repo
4. Set the following:

| Field | Value |
|---|---|
| Runtime | Python 3 |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `uvicorn main:app --host 0.0.0.0 --port 10000` |

5. Add Environment Variables:
   - `API_TOKEN` → your RapidAPI key
   - `API_HOST` → `cricbuzz-cricket.p.rapidapi.com`

---

## 📦 Requirements
fastapi
uvicorn
httpx
python-dotenv

---

## 👨‍💻 Author

**Anant Paul**
- 🐙 GitHub: [@Anant-083](https://github.com/Anant-083)
- 🎓 B.Tech CSE (AI & ML) — Semester 4

---

## ⭐ Star this repo if you like it!

*Built with ❤️ and cricket fever 🏏*