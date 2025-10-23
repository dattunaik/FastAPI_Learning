# FastAPI Learning Track

A modular learning project demonstrating **FastAPI** concepts — from basic endpoints to middleware, CRUD operations, and ML model integration.

---

## Project Structure

| Folder / File | Description |
|----------------|-------------|
| `1_basics/` | Basic FastAPI concepts — routes, query/path parameters, and simple responses. |
| `2_crud/` | CRUD operations using FastAPI — POST, GET, PUT, DELETE endpoints. |
| `3_sqlalchemy/` | Integration with **SQLAlchemy** for database ORM and persistence. |
| `4_ml_integration/` | Example of integrating a **Machine Learning model** within FastAPI endpoints. |
| `5_middleware/` | Custom middleware examples (like request timers, logging, etc.). |
| `6_dependency_injection/` | Advanced dependency injection patterns. |
| `7_config_management/` | Centralized configuration management using Pydantic. |
| `8_Authentication/` | JWT & API Key authentication examples (`8.1 JWT`, `8.2 API KEYS`). |
| `9_Testing/` | Testing using pytest and TestClient (`Unit_Testing`, `Integration_Testing`). |
| `main.py` | Root FastAPI app entry point (optional depending on setup). |
| `.gitignore` | Directories and files ignored by Git. |
| `README.md` | Project documentation. |

---

## Tech Stack

- **Python 3.10+**
- **FastAPI** — modern async web framework
- **Uvicorn** — ASGI server for FastAPI
- **SQLAlchemy** — ORM for database management
- **Pydantic** — data validation and settings
- **Authlib / python-jose** — JWT handling
- **dotenv** — environment variable management

---

## Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/fastapi-learning-track.git
cd fastapi-learning-track
