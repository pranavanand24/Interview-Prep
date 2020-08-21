n = int(input())

for i in range(n):
    a,b = list(map(float, input().split()))
    if a > 1000:
        print(a*b-((a*b)/10))
    else:
        print(a*b)
