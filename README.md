## Internship Project – Task Management API (Django/DRF)

Production‑ready Django REST API for user authentication and personal task management. Includes JWT auth, owner‑scoped Task CRUD, Swagger docs, and optional Celery + Redis for background jobs.

### Tech Stack
- **Django 5** + **Django REST Framework**
- **SimpleJWT** for authentication
- **PostgreSQL** (default in settings; SQLite can be swapped in)
- **Celery + Redis** for async tasks (welcome email after registration)
- **drf-yasg** for Swagger docs
- Optional basic HTML pages in `frontend/`

---

## How to Run Locally

### 1) Prerequisites
- Python 3.11+
- PostgreSQL (or comment the Postgres block and re‑enable SQLite in `internship_project/settings.py`)
- Redis (for Celery features) – optional

### 2) Create and activate a virtual environment
Windows PowerShell:
```powershell
python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt
```
macOS/Linux Bash:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3) Configure environment
Create a `.env` at the repo root:
```env
DJANGO_SECRET_KEY=unsafe-secret-for-dev
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=*

# Database (Postgres)
POSTGRES_DB=taskdb
POSTGRES_USER=taskuser
POSTGRES_PASSWORD=taskpass
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# Redis (for Celery)
REDIS_URL=redis://localhost:6379/0
```

If you don’t have Postgres locally, either use Docker (see below) or switch to SQLite by re‑enabling the SQLite block in `internship_project/settings.py` and commenting out the Postgres block.

### 4) Apply migrations and create a superuser
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 5) Run the app
```bash
python manage.py runserver
```

Visit:
- Django admin: `http://127.0.0.1:8000/admin/`
- Swagger docs: `http://127.0.0.1:8000/swagger/`
- Basic pages: `http://127.0.0.1:8000/`

---

## Run with Docker (optional)

The repo includes `Dockerfile` and `docker-compose.yml`.

```bash
docker compose up --build
```

## API Reference

Base URL: `http://127.0.0.1:8000`

All protected endpoints require an `Authorization: Bearer <access_token>` header obtained from the JWT token endpoint.

### Auth
- `POST /api/auth/register/`
  - Body: `{ "email": "user@example.com", "name": "Jane", "password": "Password123!" }`
  - Response: `201 Created` with user info; triggers welcome email task

- `POST /api/auth/token/`
  - Body: `{ "email": "user@example.com", "password": "Password123!" }`
  - Response: `{ "refresh": "...", "access": "..." }`

- `POST /api/auth/token/refresh/`
  - Body: `{ "refresh": "..." }`
  - Response: `{ "access": "..." }`

- `GET /api/auth/profile/`
  - Auth required
  - Response: current user profile

- `PUT /api/auth/profile/`
  - Auth required
  - Body: `{ "name": "New Name" }`
  - Response: updated profile

### Tasks
Router prefix: `/api/`

- `GET /api/tasks/`
  - List tasks for the authenticated user (owner‑scoped)

- `POST /api/tasks/`
  - Create task
  - Body: `{ "title": "Buy milk", "description": "2 liters", "status": "pending" }`

- `GET /api/tasks/{id}/`
  - Retrieve a single task owned by the user

- `PUT /api/tasks/{id}/`
  - Full update

- `PATCH /api/tasks/{id}/`
  - Partial update (e.g., `{ "status": "completed" }`)

- `DELETE /api/tasks/{id}/`
  - Delete task

### Web (optional UI)
Basic HTML views for demonstration only:
- `GET /` – Home
- `GET /register/` – Registration page
- `GET /login/` – Login page
- `GET /profile/` – Profile page
- `GET /tasks/` – Tasks page

---


## Testing
```bash
python manage.py test
```

---


## Notes & Tips
- Default permissions require authentication globally; anonymous access is allowed only for `register`, `token`, and Swagger UI (see `internship_project/urls.py`).
- Switch between Postgres and SQLite in `internship_project/settings.py` as needed.
- Swagger UI at `/swagger/` reflects the live schema and is the quickest way to explore the API.

