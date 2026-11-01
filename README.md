# PlacementPrep AI

A career and interview preparation platform for students. It combines a resume analyzer, an interview practice tool and a job-application tracker in one dashboard.

**Live demo:** https://placement-prep-ai-new.vercel.app

**Note:** The backend and database run on free hosting, so the first request after a period of inactivity may take up to a minute.

## Features
- Register/login with bcrypt-hashed passwords and JWT sessions
- Dashboard with resume score, application counts by status and recent activity
- Resume Analyzer: upload a PDF and get a 0-100 score, detected skills, strengths and suggestions
- Interview Preparation: choose a role, topic and difficulty, answer a question and get feedback
- Application Tracker: add, edit, delete and filter job applications
- Optional LLM analysis through the Claude API, with an automatic rule-based fallback when no API key is set

## Tech Stack
- **Frontend:** React (Vite), React Router
- **Backend:** Flask, Flask-JWT-Extended, SQLAlchemy, bcrypt, pypdf
- **Database:** MySQL
- **Deployment:** Vercel (frontend), Render (backend), Aiven (MySQL)

## Run Locally

**Backend**
```
cd PlacementPrepAI/backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python init_db.py
python run.py
```
Fill in your MySQL details in `.env` before running `init_db.py`.

**Frontend**
```
cd PlacementPrepAI/frontend
npm install
npm run dev
```

## Screenshots
(Add 2-3 screenshots of the dashboard, resume analyzer and application tracker here.)

## Author
Aashika Gupta
