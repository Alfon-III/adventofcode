lines = []
with open("data.txt") as file_in:   
    for line in file_in:
        lines.append(line)

i = 0
dec = inc = 0

x1 = lines[i]
x2 = lines[i + 1]
x3 = lines[i + 2]

num = len(lines) - 3
print(num)

x1 = int(lines[0])
x2 = int(lines[1])
x3 = int(lines[2])

last = x1 + x2 + x3

for n in range(num):
    print(n)
    x1 = int(lines[n + 1])
    x2 = int(lines[n + 2])
    x3 = int(lines[n + 3])

    sum = x1 + x2 + x3
 
    if sum > last:
        inc+=1
    elif sum < last:
        dec+=1
    last = sum


print("Decreased: ", dec)
print("Increased: ", inc)