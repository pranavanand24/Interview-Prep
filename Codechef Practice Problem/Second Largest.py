n = int(input())

for i in range(n):
    m = list(map(int, input().split()))
    m.sort()
    print(m[-2])