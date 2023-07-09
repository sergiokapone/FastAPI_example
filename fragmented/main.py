from fastapi import FastAPI
import uvicorn
from app.routes.hello import router as hello_router
from app.routes.sum import router as sum_router

app = FastAPI()

app.include_router(hello_router)
app.include_router(sum_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000)
