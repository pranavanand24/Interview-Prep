class Solution:
    def subtractProductAndSum(self, n):
        a = [int(x) for x in str(n)]
        return reduce((lambda x,y: x*y), a) - reduce((lambda x,y:x+y), a)