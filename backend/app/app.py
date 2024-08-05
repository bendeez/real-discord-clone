from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.user.endpoints import user_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://chat.brisbanegateway.com.au"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_router)