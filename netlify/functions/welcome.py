from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

# This handles the root of the function
@app.get("/")
def read_root():
    return {"message": "Hello World"}

# This handles the specific name Netlify uses
@app.get("/welcome")
def read_welcome():
    return {"message": "Hello from Welcome"}

handler = Mangum(app)