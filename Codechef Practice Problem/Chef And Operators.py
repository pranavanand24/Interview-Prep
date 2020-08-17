for i in range(int(input())):
    m,x = map(int, input().split())

    if m > x :
        print(">")
    elif m < x :
        print("<")
    else:
        print("=")