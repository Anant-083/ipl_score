# 🏏 IPL Score — Live Cricket Web App

<p align="center">
  <a href="https://ipl-score-dx4s.onrender.com/static/index.html">
    <img src="https://img.shields.io/badge/Live-Demo-00c853?style=for-the-badge&logo=render&logoColor=white" />
  </a>
  <a href="https://github.com/Anant-083/ipl_score">
    <img src="https://img.shields.io/badge/GitHub-Repo-181717?style=for-the-badge&logo=github" />
  </a>
</p>

---

## ✨ Overview
A minimal, real-time IPL scorecard web app built using **FastAPI** and the **Cricbuzz API**.

---

## 🚀 Live Demo  
https://ipl-score-dx4s.onrender.com/static/index.html

---

## 🎯 Features
- Live IPL match scores  
- Upcoming fixtures  
- Points table with NRR  
- Auto-refresh every 5 minutes  

---

## 🛠️ Tech Stack
- Backend: FastAPI, Python  
- Frontend: HTML, CSS, JavaScript  
- API: Cricbuzz (RapidAPI)  
- Deployment: Render  

---

## 📁 Project Structure
```
ipl_score/
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
├── engine.py
├── main.py
├── manager.py
├── requirements.txt
└── .env
```

---

## ⚙️ Setup Locally
```
git clone https://github.com/Anant-083/ipl_score.git
cd ipl_score
pip install -r requirements.txt
uvicorn main:app --reload
```

Create `.env`:
```
API_TOKEN=your_key
API_HOST=cricbuzz-cricket.p.rapidapi.com
```

Open:
```
http://localhost:8000/static/index.html
```

---

## ☁️ Deployment
```
uvicorn main:app --host 0.0.0.0 --port 10000
```

---

## 👨‍💻 Author
Anant Paul — https://github.com/Anant-083

---

## ⭐ Star this repo if you like it