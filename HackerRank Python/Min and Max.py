import numpy as np
arr = []
n,m = map(int,input().split())
for row in range(n):
    my_arr = list(map(int,input().split()))
    arr.append(my_arr)
my_array = np.array(arr)
result = np.min(my_array, axis=1)
print(max(result))



