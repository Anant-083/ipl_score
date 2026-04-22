# 🏏 IPL Score — Live Cricket Web App

A minimal, real-time IPL scorecard web app built with FastAPI and Cricbuzz API.

## 🔗 Live Demo
https://ipl-score-dx4s.onrender.com/static/index.html

## ✨ Features
- Live IPL match scores
- Upcoming IPL fixtures (fallback when nothing is live)
- IPL 2026 Points Table with NRR
- Auto-refreshes every 5 minutes
- Clean dark UI with team colors

## 🛠️ Tech Stack
- **Backend:** FastAPI, Python, httpx
- **Frontend:** HTML, CSS, Vanilla JavaScript
- **Data:** Cricbuzz API via RapidAPI
- **Deployment:** Render

## 📁 Project Structure
ipl_score/
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
├── engine.py       # API calls to Cricbuzz
├── main.py         # FastAPI app
├── manager.py      # Connection manager
├── requirements.txt
└── .env            # API keys (not committed)

## ⚙️ Setup Locally
1. Clone the repo
2. Create `.env` file:
API_TOKEN=your_rapidapi_key
API_HOST=cricbuzz-cricket.p.rapidapi.com
3. Install dependencies:
pip install -r requirements.txt
4. Run:
uvicorn main:app --reload
5. Open `http://localhost:8000/static/index.html`

## 🚀 Deployment
Deployed on Render free tier. Environment variables set in Render dashboard.

**Start command:**
uvicorn main:app --host 0.0.0.0 --port 10000

## 👨‍💻 Author
Anant Paul — [GitHub](https://github.com/Anant-083)
