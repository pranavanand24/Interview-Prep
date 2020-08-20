def prime(a):
    if a==1: return False
    else:
        for i in range(2, a):
            if a%i==0: return False
        return True

t=int(input())
while(t>0):
    t-=1
    n=int(input())
    if prime(n)==True: print("yes")
    else: print("no")