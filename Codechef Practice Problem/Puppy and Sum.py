def sumre(n):
    return (n*(n+1))//2
for _ in range(int(input())):
    d,n=map(int,input().split())
    x=n
    for i in range(d):
        x=sumre(x)
    print(x)

