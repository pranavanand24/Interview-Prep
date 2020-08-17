x,y=map(float,input().split())
if x%5==0:
    if (x+.5)<=y:
        y -=(x+.5)
print(y)
