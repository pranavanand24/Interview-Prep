import math
m = int(input())

for i in range(m):
    a,b = list(map(int, input().split()))
    q=math.gcd(a,b)
    r=(a*b)//q
    print(q,r)