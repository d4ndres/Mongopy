#FastAPI
from fastapi import FastAPI
from routes.user import user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
	title = "Rest API with FastAPI and MongoDB",
	description = "this is a simple Rest API using fastapi and MongoDB",
	version="0.0.2"
	)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user)