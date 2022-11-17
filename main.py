#FastAPI
from fastapi import FastAPI
from routes.user import user

app = FastAPI(
	title = "Rest API with FastAPI and MongoDB",
	description = "this is a simple Rest API using fastapi and MongoDB",
	version="0.0.1"
	)
app.include_router(user)