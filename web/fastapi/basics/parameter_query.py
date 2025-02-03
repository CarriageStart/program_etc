from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World~!"}

@app.get("/users/{user_id}/items/{item_name}")
def read_root(user_id, item_name):
    return {"user_id": user_id, "item_name": item_name}

@app.get("/users/{user_id}/items/{item_name}")
def read_user_item(user_id, item_name):
    return {"user_id": user_id, "item_name": item_name}

@app.get("/items1/")
def read_items(skip, limit):
    return {"skip": skip, "limit" : limit}

@app.get("/items/")
def read_items(skip=0, limit=20):
    return {"skip": skip, "limit" : limit}
