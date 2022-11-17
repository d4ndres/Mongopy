
#Al especificar esta funcion, Se genera la documentacion.
def userEntity( item ) -> dict:
	return {
		"_id": str(item["_id"]),
		"name": item["name"],
		"email": item["email"],
		"password": item["password"],

	}

def usersEntity( entity ) -> dict:
	return [userEntity(item) for item in entity ]