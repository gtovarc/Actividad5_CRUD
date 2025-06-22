## Actividad 5: API con CRUD
**Schemas**
--
    Alumno:
		    { 
			    Matricula (int),
			    Nombre (string),
			    Edad (int),
			    Facultad (string),
			    Grado (string),
			    Carrera (string),
			    Genero (string),
			    Correo (string),
			    Promedio (float),
			    Semestre (integer)
			 }
     
---
**default**
--
**1. GET**

*GET /alumnos/*

Parámetros: 

    Sin parámetros

Respuesta:
```json
[
...
,{
  "Matricula":202163319,
  "Nombre":"ALTAMIRANO, APEL NOBLE",
  "Edad":22,
  "Facultad":"Ciencias de la computación",
  "Grado":"Licenciatura",
  "Carrera":"Ing. Tecnologias de la Información",
  "Genero":"Masculino",
  "Correo":"nobb.altamirano@alumno.buap.mx",
  "Promedio":7,
  "Semestre":6
},
...
]
```

---
**2. POST**

*POST /alumnos/*
Parámetros: 

    Matricula (int),
    Nombre (string),
    Edad (int),
    Facultad (string),
    Grado (string),
    Carrera (string),
    Genero (string),
    Correo (string),
    Promedio (float),
    Semestre (integer)

Respuesta:
```json
{
  "Matricula":202163319,
  "Nombre":"ALTAMIRANO, APEL NOBLE",
  "Edad":22,
  "Facultad":"Ciencias de la computación",
  "Grado":"Licenciatura",
  "Carrera":"Ing. Tecnologias de la Información",
  "Genero":"Masculino",
  "Correo":"nobb.altamirano@alumno.buap.mx",
  "Promedio":7,
  "Semestre":6
}
```
---
**3. PUT**

*PUT /alumnos/*
Parámetros: 

    Matricula (int),
    Nombre (string),
    Edad (int),
    Facultad (string),
    Grado (string),
    Carrera (string),
    Genero (string),
    Correo (string),
    Promedio (float),
    Semestre (integer)

Respuesta:
```json
{
  "Matricula":202163319,
  "Nombre":"ALTAMIRANO, APEL NOBLE",
  "Edad":22,
  "Facultad":"Ciencias de la computación",
  "Grado":"Licenciatura",
  "Carrera":"Ing. Tecnologias de la Información",
  "Genero":"Masculino",
  "Correo":"nobb.altamirano@alumno.buap.mx",
  "Promedio":7,
  "Semestre":6
}
```
---
**4. DELETE**

*DELETE /alumnos/*
Parámetros: 

    Matricula (int),
    Nombre (string),
    Edad (int),
    Facultad (string),
    Grado (string),
    Carrera (string),
    Genero (string),
    Correo (string),
    Promedio (float),
    Semestre (integer)

Respuesta:
```json
{
  "message": "Alumno eliminado"
}
```

