n,k = list(map(int, input().split()))
c=0
for i in range(n):
    m=int(input())
    if m%k==0:
        c+=1
print(c)


