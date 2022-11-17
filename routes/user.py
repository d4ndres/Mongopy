from fastapi import APIRouter, Response, status
from config.db import db
from schemas.user import userEntity, usersEntity
from models.user import User
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()

@user.get('/users', tags=["users"])
def find_all_users():
	return usersEntity(db.users.find())


@user.post('/users',  response_model=User, tags=["users"])
def create_user(user: User):
	new_user = dict( user )
	id = db.users.insert_one(new_user).inserted_id
	return userEntity(db.users.find_one({"_id": id}))

@user.get('/users/{id}', response_model=User, tags=["users"])
def find_user(id: str):
	return userEntity(db.users.find_one({"_id": ObjectId(id)}))

@user.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
def delete_user(id: str):
	db.users.find_one_and_delete({"_id": ObjectId(id)})
	return Response(status_code=HTTP_204_NO_CONTENT)

@user.put('/users/{id}', response_model=User, tags=["users"])
def update_user(id:str, user: User):
	db.users.find_one_and_update(
		{"_id": ObjectId(id)}, 
		{"$set": dict(user)}
	)
	return userEntity( db.users.find_one({"_id": ObjectId(id)}) )