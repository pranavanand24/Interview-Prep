n = int(input())
m = 0
while m < n:
    s = input()

    if s == s[::-1]:
        print("wins")
    else:
        print("loses")
    m += 1



