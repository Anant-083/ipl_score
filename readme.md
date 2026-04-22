# 🏏 IPL Score Live

A real-time IPL 2026 dashboard providing live scorecards, detailed points tables, and upcoming fixtures. Built with a high-performance FastAPI backend and a sleek, responsive vanilla JS frontend.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=flat-square&logo=fastapi)
![Render](https://img.shields.io/badge/Deployed-Render-purple?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## 🌐 Live Demo

**👉 [View Live Project](https://ipl-score-dx4s.onrender.com/static/index.html)**

> ⚠️ **Note:** Hosted on Render's free tier. If the site is "sleeping," it may take **30–50 seconds** to spin up on the first visit.

---

## 📸 Preview

| Live Match Dashboard | Points Table & Standings |
|---|---|
| ![Scorecard Placeholder](https://via.placeholder.com/400x250?text=Live+Scorecard+Preview) | ![Table Placeholder](https://via.placeholder.com/400x250?text=IPL+Points+Table+Preview) |

---

## ✨ Features

- 🔴 **Live Ball-by-Ball Updates** — Real-time match data fetched via Cricbuzz API.
- 📅 **Smart Fixtures** — Automatically displays upcoming matches when no game is live.
- 📊 **Advanced Standings** — Points table with Wins, Losses, and Net Run Rate (NRR).
- 🎨 **Team-Specific UI** — Dynamic color badges tailored to each IPL franchise.
- ⚡ **Optimized Performance** — Auto-refreshes every 5 minutes to stay current without hitting API limits.
- 📱 **Mobile First** — Fully responsive design for checking scores on the go.
- 🌙 **Modern Dark Theme** — Minimalist aesthetic designed for night-match viewing.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | FastAPI (Python 3.11), `httpx` for async requests |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Data Source** | Cricbuzz API via RapidAPI |
| **Deployment** | Render (Web Service) |
| **Environment** | `python-dotenv` for secure credential management |

---

## 📁 Project Structure

```text
ipl_score/
├── frontend/
│   ├── index.html       # Main UI structure
│   ├── style.css        # Custom CSS with Dark Mode variables
│   └── app.js           # Fetch logic & DOM manipulation
├── engine.py            # API Wrapper & Data Parsing
├── main.py              # FastAPI Application & Static Routing
├── manager.py           # Logic for handling concurrent updates
├── requirements.txt     # Dependency manifest
├── .env.example         # Template for API keys
└── README.md