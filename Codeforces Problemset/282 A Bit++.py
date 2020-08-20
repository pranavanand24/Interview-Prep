x = 0
inp = range(int(input()))


for i in inp:
    y = input().lower()
    if y == "++x" or y == "x++":
        x += 1
    elif y == "--x" or y == "x--":
        x -= 1

print(x)