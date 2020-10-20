def addTwoDigits(n):
    if n == 0:
        return 0
    return n%10 + addTwoDigits(n//10)
