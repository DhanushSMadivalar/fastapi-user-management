from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from models import User, UserUpdate

#instance of FastAPI
app = FastAPI()

# In-memory database
users_db = {}


@app.post("/users/", status_code=201) #create user 
def create_user(user: User):
    if user.id in users_db:
        raise HTTPException(status_code=400, detail="User ID already exists")
    users_db[user.id] = user
    return {"message": "User created successfully"}

@app.get("/users/{id}") #get user using id
def get_user(id: int):
    user = users_db.get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/users/search/{name}", response_model=List[User]) #get user using name
def search_users(name: str):
    results = [user for user in users_db.values() if name.lower() in user.name.lower()]
    return results

@app.put("/users/{id}") #update the user using his id and provide the details to be updated in request body
def update_user(id: int, user_update: UserUpdate):
    user = users_db.get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    update_data = user_update.dict(exclude_unset=True)
    updated_user = user.copy(update=update_data)
    users_db[id] = updated_user
    return {"message": "User updated successfully"}

@app.delete("/users/{id}") #delete user using his id
def delete_user(id: int):
    if id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[id]
    return {"message": "User deleted successfully"}
