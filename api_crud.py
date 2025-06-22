#Importar el framework de fastapi
from fastapi import FastAPI, HTTPException
#Crear objeto a partir de la clase FastAPI
app = FastAPI()
#importar pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel, ValidationError

#importar pandas 
import pandas as pd
#Importar la librería para manejar archivos
import os   

#---------------------------------------------------------------------
 
 #Actividad 5: API con CRUD 
  
#Definir la clase Alumno para el modelo de datos
class Alumno(BaseModel):
    Matricula: int
    Nombre: str
    Edad: int
    Facultad: str
    Grado: str
    Carrera: str
    Genero: str
    Correo: str
    Promedio: float
    Semestre: int

#Copiar los datos del csv de los alumnos y convertirlo en una lista compatible con el modelo Alumno
def cargar_datos_alumnos():
    df =pd.read_csv('BD_E6_v2.csv')
    lista_alumnos = df.to_dict(orient='records')
    return lista_alumnos

#Lista para almacenar los alumnos
alumnos = cargar_datos_alumnos()

# 1. Obtener todos los alumnos
@app.get("/alumnos/")
def get_alumnos():
    return alumnos

# 2. Agregar un nuevo alumno
@app.post("/alumnos/")
async def nuevo_alumno(alumno: Alumno):
    # Verificar si el alumno ya existe por matrícula
    for saved_user in alumnos:
        if saved_user["Matricula"] == alumno.Matricula:
            return {"error": "El alumno ya existe"}
    # Si no existe, agregarlo
    alumnos.append(alumno.model_dump())
    return alumno

# Modificar un alumno existente
@app.put("/alumnos/")
async def modificar_alumno(alumno: Alumno):
    found = False #Bandera para verificar si se encontró el alumno
    
    for index, saved_user in enumerate(alumnos):
        if saved_user["Matricula"] == alumno.Matricula:
            alumnos[index] = alumno.model_dump()
            found = True
    if not found:
        return {"error": "No se ha actualizado el alumno"}
    return alumno

# Eliminar un alumno
@app.delete("/alumnos/")
async def eliminar_alumno(alumno: Alumno):
    # Verificar si el alumno existe
    found = False
    for index, saved_user in enumerate(alumnos):
        if saved_user["Matricula"] == alumno.Matricula:
            del alumnos[index]
            found = True
            break
    if not found:
        return {"error": "No se ha eliminado el alumno"}
    return {"message": "Alumno eliminado"}
