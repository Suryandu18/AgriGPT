from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to AgriGPT Backend"}

@app.get("/health")
def health_check():
    return {"status": "Server running"}
