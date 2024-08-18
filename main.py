from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return{"details": "Hello from Ghost"}

@app.get("/hi")
def index():
    return{"details": "Welcome"}


uvicorn.run(app, host="0.0.0.0", port=8000)