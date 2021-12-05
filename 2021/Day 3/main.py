import statistics

lines = []
with open("Day 3/data.txt") as file_in:   
    for line in file_in:
        lines.append(line)

aux = ""

for n in range(12):
    #Array de caracteres del n elemento de cada fila (leer en vertical)
    letters_list = [x[n] for x in lines if len(x)>0]
    #Se obtiene el caracter (0 o 1) más repetido de la lista
    aux = aux + statistics.mode(letters_list)
    
print(aux)

#Aux devuelve el código en decimal.
#Traducir con la calculadora de programador de windows
#Repetir el proceso con el binario en NOT
