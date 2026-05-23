# Name Generator

Minimal fullstack Chinese name generator.

## Structure

- `frontend/`: static web UI
- `backend/`: local Flask API for development
- `api/index.py`: Vercel Python serverless API entry

## Local Development

1. Start backend:

```bash
cd backend
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```

2. Start frontend in a second terminal:

```bash
cd frontend
python -m http.server 5173
```

3. Open `http://127.0.0.1:5173`.

## Deploy Plan (Vercel)

- Frontend project: set Root Directory to `frontend/`
- Backend project: set Root Directory to repository root and use `vercel.json`
- Backend endpoint will be `/api/*` served by `api/index.py`

## Domain

- Frontend domain: `dldl66.cc.cd`
- Backend domain: `api.dldl66.cc.cd`

`frontend/app.js` is already configured:
- local development uses `http://127.0.0.1:5000`
- production uses `https://api.dldl66.cc.cd`
