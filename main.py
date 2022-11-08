#Python
from typing import Optional
from enum import Enum

#Pydantic
from pydantic import BaseModel
from pydantic import Field

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Path
from fastapi import Query

app = FastAPI()


#Models

class HairColor(Enum):
	white = "white"
	brown = "brown"
	black = "black"
	blonde = "blonde"
	red = "red"


class Person(BaseModel):
	nombre: str = Field(..., min_length = 1, max_length=50)
	apellido: str = Field(..., min_length = 1, max_length=50)
	edad: int = Field(..., gt=0, lt=120)
	color_pelo: Optional[HairColor] = Field(default=None)
	es_casado: Optional[bool] = Field(default=None)


class Location(BaseModel):
	city: str
	state: str
	country: str


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


# Validations: request Body
@app.put("/person/{person_id}")
def update_person(
	person_id: int = Path(
		...,
		title="Person ID",
		description = "This is the person ID",
		gt=0

		),
	person: Person = Body(...),
	location: Location = Body(...)
):
	results = person.dict()
	results.update( location.dict() )
	return results