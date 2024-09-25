# Definimos el nombre del archivo
file_name = "ejemplo_escritura.txt"

# Modo de apertura: "w" para escritura (write)
archivo_escritura = open(file_name, "w")

# Método write(): escribir una línea a la vez
archivo_escritura.write("NOMBRE: Domenica\n")
archivo_escritura.write("EDAD: 20\n")
archivo_escritura.write("CIUDAD: Quito\n")
archivo_escritura.write("PROFESION: Costurera\n")
archivo_escritura.write("TELEFONO: 0952365418\n")
# Cerramos el archivo de escritura
archivo_escritura.close()

# Modo de apertura: "r" para lectura (read)
archivo_lectura = open(file_name, "r")

# Leemos el contenido del archivo
lineas = archivo_lectura.readlines()
archivo_lectura.close()
# Filtramos las líneas para eliminar la línea "EDAD: 20"
lineas_modificadas = [linea for linea in lineas if "EDAD: 20" not in linea]
# Modo de apertura: "w" para escribir el contenido modificado de nuevo
archivo_escritura = open(file_name, "w")
archivo_escritura.writelines(lineas_modificadas)

# Cerramos el archivo de escritura
archivo_escritura.close()

# Leemos y mostramos el contenido para verificar
archivo_lectura = open(file_name, "r")
contenido = archivo_lectura.read()
print(contenido)

# Cerramos el archivo de lectura
archivo_lectura.close()
