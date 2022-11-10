
def userEntity( item ) -> dict:
	return {
		"id": item["id"],
		"name": item["name"],
		"email": item["email"],
		"password": item["password"],

	}

def usersEntity( entity ) -> dict:
	[userEntity(item) for item in entity ]