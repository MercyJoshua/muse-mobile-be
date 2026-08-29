from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.auth import router as auth_router

app = FastAPI()

# Allow connections from mobile/web client
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI(
    title="Muse API",
)


app.include_router(auth_router)


@app.get("/api/health")
def health_check():
    return {"status": "ok", "message": "FastAPI is running"}

""" @app.post("/api/register")
def register_user():
    return {"status": "ok", "message": "User registered successfully"}

@app.post("/api/login")
def login_user():
    return {"status": "ok", "message": "User logged in successfully"}

@app.get("/api/me")
def get_users():
    return {"status": "ok", "message": "List of users"} """