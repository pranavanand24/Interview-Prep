if __name__ == '__main__':
    n = int(input())
    print(hash(tuple(int(x) for x in input().split())))
