import math
import os
import random
import re
import sys


def kangaroo(x1, v1, x2, v2):
    for n in range(10000):
        if((x1+v1)==(x2+v2)):
            return  "YES"
        x1+=v1
        x2+=v2
    return "NO"