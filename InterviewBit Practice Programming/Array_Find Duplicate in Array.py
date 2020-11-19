def repeatedNumber(self, A):
    sumOfList = sum(A)
    n = len(A)
    sumOfRange = int(n * (n + 1) / 2) - n
    return sumOfList - sumOfRange