# PlacementPrep AI

A career and interview preparation platform for students. It combines a resume analyzer,
an interview practice tool and a job-application tracker in one dashboard.

**Live demo:** (add your Vercel link here once deployed)
**Note:** The backend runs on a free host, so the first request after a period of
inactivity may take up to a minute.

## Features
- Register/login with bcrypt-hashed passwords and JWT sessions
- Dashboard with resume score, application counts by status and recent activity
- Resume Analyzer: upload a PDF and get a 0-100 score, detected skills, strengths and suggestions
- Interview Preparation: choose a role, topic and difficulty, answer a question and get feedback
- Application Tracker: add, edit, delete and filter job applications
- Optional LLM analysis through the Claude API, with an automatic rule-based fallback
  when no API key is set

## Tech Stack
React (Vite), React Router, Flask, Flask-JWT-Extended, SQLAlchemy, MySQL, bcrypt, pypdf

## Run Locally
**Backend**
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env     (then fill in your MySQL details)
python init_db.py
python run.py

**Frontend**
cd frontend
npm install
npm run dev

## Screenshots
(add 2-3 screenshots here)
