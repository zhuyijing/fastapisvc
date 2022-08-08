from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def read_root():
    return {"msg": "Welcome to Home Page, from {}".format(os.environ.get('SECRET_USER', 'anonymous'))}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

