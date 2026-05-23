# Name Generator

Minimal fullstack Chinese name generator.

## Structure

- rontend/: static web UI
- ackend/: Flask API

## Local Development

1. Start backend:

`ash
cd backend
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
`

2. Start frontend in a second terminal:

`ash
cd frontend
python -m http.server 5173
`

3. Open http://127.0.0.1:5173.

## Deploy Plan

- Frontend: deploy rontend/ to Vercel (or Cloudflare Pages)
- Backend: deploy ackend/ to Render or Railway and get public API URL
- Update rontend/app.js piBase to backend URL

## Domain

After frontend deploy, set custom domain dldl66.cc.cd on your frontend platform and add DNS records in your domain provider.
