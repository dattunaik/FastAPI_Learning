from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Fake in-memory "database"
users = {}

# Pydantic model for request body
class User(BaseModel):
    name: str
    age: int

# 1. GET → Retrieve Data
# ✅ Returns 200 OK if user exists.
# ❌ Returns 404 Not Found if user doesn’t exist.
@app.get("/users/{user_id}", status_code=200)
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")  # 404 Example
    return {"user_id": user_id, "data": users[user_id]}

#--------------------------------------

# 2. POST → Create Data
# ✅ Returns 201 Created when a new user is added.
# ❌ Returns 400 Bad Request if user already exists.
@app.post("/users", status_code=201)
def create_user(user_id: int, user: User):
    if user_id in users:
        raise HTTPException(status_code=400, detail="User already exists")  # 400 Example
    users[user_id] = user.dict()
    return {"message": "User created", "user_id": user_id}

#--------------------------------------
# 3. PUT → Update (replace) Resource
# ✅ Returns 200 OK when user is updated.
# ❌ Returns 404 Not Found if user doesn’t exist.

@app.put("/users/{user_id}", status_code=200)
def update_user(user_id: int, user: User):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = user.dict()  # Full replace
    return {"message": "User updated", "user_id": user_id}

#--------------------------------------
# 4. PATCH → Partial Update
# ✅ Updates only given fields.
# Example: PATCH { "age": 30 } → only updates age.

@app.patch("/users/{user_id}", status_code=200)
def patch_user(user_id: int, user: dict):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id].update(user)  # Partial update
    return {"message": "User partially updated", "user_id": user_id}


#--------------------------------------
# 5. DELETE → Remove Resource
# ✅ Returns 204 No Content when deleted.
# ❌ Returns 404 Not Found if user doesn’t exist.

@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return {"message": "User deleted"}  # Note: with 204, body is usually empty


#--------------------------------------
# 6. HEAD → Headers Only
# ✅ Returns only headers (like 200 OK and content type).
@app.head("/health")
def head_health():
    return {"status": "ok"}  # FastAPI automatically strips body for HEAD
