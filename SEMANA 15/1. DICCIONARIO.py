# Crear un diccionario
informacion_personal = {
    "nombre": "DOMENICA",
    "edad": 20,
    "ciudad": "QUITO",
    "profesion": "COSTURERA"
}

# Acceder y modificar el valor asociado con la clave "ciudad"
informacion_personal["ciudad"] = "CUENCA"

# Agregar una nueva clave-valor al diccionario para la "profesion"
informacion_personal["profesion"] = "COSTURERA"

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0985236547"

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)
