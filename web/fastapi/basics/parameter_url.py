from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World~!"}

# Receiving URL Parameters : The position of the parameter specified
@app.get("/users/{user_id}/items/{item_name}")
def read_root(user_id, item_name):
    return {"user_id": user_id, "item_name": item_name}


