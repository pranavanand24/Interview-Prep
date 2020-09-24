class Solution:
    
    def solve(self, A):
        minn, maxx = sys.maxsize, -sys.maxsize
    
        for i in range(len(A)):
            if A[i] < minn:
                minn = A[i]
            if A[i] > maxx:
                maxx = A[i]
                
        
        return maxx+minn