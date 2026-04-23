from fastapi import FastAPI, UploadFile, File
from disease_detection import detect_disease
from chatbot import ask_agrigpt

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to AgriGPT Backend"}

@app.get("/health")
def health_check():
    return {"status": "Server running"}

# Plant Disease Detection API
@app.post("/detect-disease")
async def detect(image: UploadFile = File(...)):
    
    result = detect_disease(image)
    
    return result


# Agriculture Chatbot API
@app.get("/ask-agrigpt")
def ask(question: str):
    
    answer = ask_agrigpt(question)
    
    return {"response": answer}
