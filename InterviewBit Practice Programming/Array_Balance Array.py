class Solution:
    def solve(self, A):
        n = len(A)
        even = 0
        odd = 0
        i = 0
        while i<n:
            if i%2==0:
                odd += A[i]
            else:
                even += A[i]
            i += 1
        
        ans = 0     
        x = 0
        y = 0
        i = 0
        while i<n:
            if i%2==0:
                odd -= A[i]
            else:
                even -= A[i]
                
            if odd+x==even+y:
                ans += 1
            if i%2==0:
                y += A[i]
            else:
                x += A[i]
            i += 1
        return ans