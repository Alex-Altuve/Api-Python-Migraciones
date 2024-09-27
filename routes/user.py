from fastapi import APIRouter, Response
from config.db import conn
from models.user import users
from schemas.user import User
from typing import List
from cryptography.fernet import Fernet
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

key = Fernet.generate_key()
f = Fernet(key)

user = APIRouter()

@user.get("/users",tags=["Usuarios"], response_model= List[User])
def get_users():
    return conn.execute(users.select()).fetchall()


@user.post("/users",tags=["Usuarios"], response_model=User) 
def create_user(user: User):
    new_user = {"name": user.name, 
                "email": user.email,
                "password":f.encrypt(user.password.encode("utf-8"))}
    
    result = conn.execute(users.insert().values(new_user))
    conn.commit()
    # Obtiene el ID del nuevo usuario
    new_user_id = result.inserted_primary_key[0]  
    return conn.execute(users.select().where(users.c.id == new_user_id)).first()
  
@user.get("/users/{id}",tags=["Usuarios"], response_model=User, description="Get a single user by Id")
def get_user(id: str):
   return conn.execute(users.select().where(users.c.id == id)).first()
   
@user.delete("/users/{id}",tags=["Usuarios"], response_model=User, description="delete a single user")
def get_user(id: str):
   conn.execute(users.delete().where(users.c.id == id))
   conn.commit()
   return Response(status_code=HTTP_204_NO_CONTENT)

@user.put("/users/{id}",tags=["Usuarios"], response_model=User,description="Update a User by Id")
def update_user(id: str, user: User):
    conn.execute(
        users.update()
        .values(name=user.name, 
                email=user.email, 
                password=f.encrypt(user.password.encode("utf-8")))
        .where(users.c.id == id))
    conn.commit()

    return conn.execute(users.select().where(users.c.id == id)).first()
   