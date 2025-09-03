from fastapi import FastAPI
from routes.index import user
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import app.auth.auth_handler as auth
from config.db import Base, engine

load_dotenv()

app = FastAPI()

# Drop and recreate database tables (for development)
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
app.include_router(auth.router)

origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user)