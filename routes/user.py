from fastapi import APIRouter
from config.db import conn
from schemas.user import userEntity, usersEntity
from models.user import User

user = APIRouter()


@user.get('/users')
def find_all_users():
	return usersEntity(conn.local.user.find())

@user.post('/users')
def create_user(user: User):
	new_user = dict( user )

	id = conn.local.user.insert_one(new_user).inserted_id

	return str(id)

@user.get('/users/{id}')
def find_user():
	return 'xd'

@user.delete('/users/{id}')
def delete_user():
	return 'xd'

@user.put('/users/{id}')
def update_user():
	return 'xd'