lines = []
with open("Day 2/data.txt") as file_in:   
    for line in file_in:
        lines.append(line)

coord = {
  "forward": 0,
  "up": 0,
  "down": 0,
  "aim": 0

}

for line in lines:
    aux = line.split(" ")
    dir = aux[0]
    num = aux[1]

    if dir == "forward":
        coord["forward"] += int(num)
        coord["down"] += int(num) * coord["aim"]
    elif dir == "up":
        coord["aim"]-= int(num)
    elif dir == "down":
        coord["aim"]+= int(num)

print("Forward: ", coord["forward"])
print("Depth: ", coord["down"])
print("Solution: ", (coord["down"] - coord["up"]) *  coord["forward"])        

print(coord)
