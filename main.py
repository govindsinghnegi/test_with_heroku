import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

def create_df_from_dict():
    data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
    return pd.DataFrame.from_dict(data)

app = FastAPI()

class Value(BaseModel):
    value: int

@app.get("/")
async def say_hello():
    return {"greeting": "Hello World!"}

@app.post("/{path}")
async def exercise_function(path: int, query: int, body: Value):
    return {"path": path, "query": query, "body": body}