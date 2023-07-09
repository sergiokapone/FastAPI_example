from fastapi import FastAPI
import uvicorn
from dataclasses import dataclass

app = FastAPI()


@dataclass
class Numbers:
    a: int
    b: int


@app.get("/")
async def hello():
    return {"hello": "world"}


@app.post("/sum")
async def sum(numbers: Numbers):
    return {"hello": numbers.a + numbers.b}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000)
