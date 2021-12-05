import statistics

lines = []
with open("Day 3/data.txt") as file_in:   
    for line in file_in:
        lines.append(line)

aux = ""

for n in range(12):
    letters_list = [x[n] for x in lines if len(x)>0]
    aux = aux + statistics.mode(letters_list)
    print(aux)

