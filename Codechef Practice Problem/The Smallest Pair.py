n = int(input())

for i in range(n):
    r = int(input())
    q = list(map(int, input().split()))
    q = sorted(q)

    m1 = q[0]
    m2 = q[1]
    z = m1 + m2
    print(z)