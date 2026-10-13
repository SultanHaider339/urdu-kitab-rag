from fastapi import FastAPI

app = FastAPI(
    title = "UrduKitab AI",
    description = "UrduKitab AI is a web application that provides AI-powered features for Urdu literature and content.",
    version = "1.0.0"
)

@app.get("/")
def home():
    return {
    "message": "Welcome to UrduKitab AI!",
    "Status": "success"
    }