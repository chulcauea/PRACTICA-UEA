columna_a = [1,20,6]
columna_b = [100,94,52]
columna_c = [6,25,22]

matriz =[columna_a,columna_b,columna_c]
print(matriz [2] [1])

#Bubble Sort de la columna b
print("Ordenamiento de la columna B")
print(columna_b)
for i in range (len(columna_b)-1):
    for j in range(len(columna_b)-1):
        if columna_b[j] > columna_b[j+1]:
            temporal = columna_b[j]
            columna_b[j] = columna_b[j+1]
            columna_b[j + 1] = temporal
print (columna_b)