from math import ceil

n, m, a = map(int, input().split())

xn = ceil(n / a)
xm = ceil(m / a)

out = xn * xm

print(out)