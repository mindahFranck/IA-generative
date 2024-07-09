from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import detect, generate

app = FastAPI()

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusion des routes
app.include_router(detect.router)
app.include_router(generate.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the License Plate Detection API"}
