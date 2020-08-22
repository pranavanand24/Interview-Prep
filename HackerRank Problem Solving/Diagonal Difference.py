import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    prim = 0
    sec = 0
    length = len(arr[0])
    for count in range(length):
        prim += arr[count][count]
        sec += arr[count][(length - count -1)]
    return abs(prim - sec)