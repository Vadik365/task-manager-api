# Task Planner

A full-stack task planner application for managing goals and tasks, tracking progress, and organizing daily activities.

## Tech Stack

**Backend**
- Python, Django, Django REST Framework
- PostgreSQL
- JWT Authentication (SimpleJWT)
- Docker

**Frontend**
- React
- Axios
- React Router

## Features

- User registration and authentication via JWT
- Create, edit and delete goals with categories
- Add and complete tasks within goals
- Filter goals by category
- Progress tracking per goal
- Dark / Light mode
- Auto token refresh

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/register/` | Register new user |
| POST | `/api/token/` | Get access & refresh tokens |
| POST | `/api/token/refresh/` | Refresh access token |
| GET/POST | `/api/goals/` | List / create goals |
| GET/PUT/DELETE | `/api/goals/<id>/` | Goal detail |
| GET/POST | `/api/tasks/` | List / create tasks |
| GET/PUT/DELETE | `/api/tasks/<id>/` | Task detail |
| GET | `/api/categories/` | List categories |

## Getting Started

### Backend
```bash
docker-compose up --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

### Frontend
```bash
cd task-manager-frontend
npm install
npm start
```

Open `http://localhost:3000`

## Status

In development — core features complete, improvements ongoing.
