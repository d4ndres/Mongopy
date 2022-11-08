#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Path
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
		name: Optional[str] = Query(
			None, 
			min_length = 1, 
			max_length = 50,
			title = "Person Name",
			description = "This is the person name. Its between 1 and 50 characters"
			),
		age: int = Query(
			...,
			title = "Person Age",
			description = "This is the age. Its requiert"
			),

		):
	return { name: age }

#Validations: Path Paramethers
@app.get('/person/detail/{person_id}')
def show_person(
		person_id: int = Path(

			..., 
			gt=0,
			title = "Person ID",
			description = "This is the person ID . Its requiert"

			)
		):
	return { person_id: "it exists!"}