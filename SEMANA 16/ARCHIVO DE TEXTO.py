# Escritura de Archivo de Texto
with open('my_notes.txt', 'w') as file:
    file.write("Nota 1: Dejar a mi hijo en la escuela de futbol.\n")
    file.write("Nota 2: Visitar a mi hermana.\n")
    file.write("Nota 3: Hacer deberes hasta el domingo.\n")
    file.write("Nota 3: Acabamos el semestre la proxima semana.\n")
    file.write("Nota 3: Salir a pasear con mi familia.\n")

# Lectura de Archivo de Texto
with open('my_notes.txt', 'r') as file:
    for line in file:
        print(line.strip())
