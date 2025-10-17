#  FastAPI Learning Track

A modular learning project demonstrating **FastAPI** concepts — from basic endpoints to middleware, CRUD operations, and ML model integration.

---

##  Project Structure

| Folder / File | Description |
|----------------|-------------|
| `1_basics/` | Basic FastAPI concepts — routes, query/path parameters, and simple responses. |
| `2_crud/` | CRUD operations using FastAPI — covers POST, GET, PUT, DELETE endpoints. |
| `3_sqlalchemy/` | Integration with **SQLAlchemy** for database ORM and persistence. |
| `4_ml_integration/` | Example of integrating a **Machine Learning model** within FastAPI endpoints. |
| `5_middleware/` | Custom middleware examples (like request timers, logging, etc.). |
| `main.py` | Root FastAPI app entry point (optional depending on setup). |
| `.gitignore` | File specifying directories and files to be ignored by Git. |
| `README.md` | Project documentation (this file). |

---

##  Tech Stack

- **Python 3.10+**
- **FastAPI** — modern, async web framework
- **Uvicorn** — ASGI server for running FastAPI apps
- **SQLAlchemy** — ORM for database management
- **Pydantic** — data validation and serialization
- **keras/pikle/joblib** *(optional)* — for ML model integration

---

##  Setup Instructions

### 1️ Clone the Repository
```bash
git clone https://github.com/<your-username>/fastapi-learning-track.git
cd fastapi-learning-track
