count = 0
for i in range(int(input())):
    a = input()
    if a.count('1') >= 2:
        count += 1
print(count)
