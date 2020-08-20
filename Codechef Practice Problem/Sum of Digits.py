c = int(input())

for i in range(c):
    n = int(input())
    s = 0
    while n!=0:
        s = s + int(n%10)
        n = int(n/10)
    print(s)
