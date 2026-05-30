from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

# root_path is CRITICAL for Netlify functions to match routes correctly
app = FastAPI(root_path="/.netlify/functions/welcome")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root(name: str = "Guest"):
    return {
        "status": "success",
        "message": f"Welcome, {name}! Your FastAPI app is running on Netlify Functions.",
        "docs": "/docs"
    }

@app.get("/hello")
def say_hello():
    return {"message": "Hello from a sub-route!"}

# This is the handler Netlify looks for
handler = Mangum(app)