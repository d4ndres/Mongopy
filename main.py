#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body
from fastapi import Query

app = FastAPI()


#Models
class Person(BaseModel):
	nombre: str
	apellido: str
	edad: int
	color_pelo: Optional[str] = None
	es_casado: Optional[bool] = None


#Path operation
@app.get("/")
def home(): #Path decoration function
	return {
	"Hellow": "World",
	"PruebaAPI": True
	} 

#Request and Response Body
@app.post("/person/new")
def create_person( person: Person = Body(...)):
	return person

#Validations: Query Paramethers

#"person/detail?name=Miguel&age=25"
@app.get('/person/detail')
def show_person(
	name: Optional[str] = Query(None, min_length=1, max_length=50),
	age: int = Query(...)
	):
	return { name: age }