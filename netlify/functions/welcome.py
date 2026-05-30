from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

app = FastAPI()

# Enable CORS so your frontend projects can communicate with it
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# This targets the absolute root URL "/"
@app.get("/")
def read_root(name: str = "Guest"):
    return {"message": f"Welcome, {name}! Great to have you here."}

# The bridge wrapper Netlify needs
handler = Mangum(app)