from fastapi import FastAPI, UploadFile, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
#------------------------------------------------------
from routes.user import user


app = FastAPI( title="Api Python")


#para inscluir rutas
app.include_router(user)

# comando para compilar 
## fastapi dev nombre.py
## uvicorn main:app --reload

## para instalar los txt 
## pip install -r ./requirements.txt
# CORS


# origins = [
#     "http://localhost",
#     "http://localhost:3000",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

