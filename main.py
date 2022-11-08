#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body

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

@app.post("/person/new")
def create_person( person: Person = Body(...)):
	return person