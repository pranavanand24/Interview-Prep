from cmath import phase
print((lambda x: '%.3f\n%.3f' % (abs(x), phase(x)))(complex(input())))