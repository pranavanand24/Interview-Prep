def maxSubArray(self, A):
        max_so_far = A[0]
        current_max = A[0]
        for i in range(1,len(A)):
            current_max = max(current_max + A[i], A[i])
            max_so_far = max(max_so_far, current_max)
        
        return max_so_far
    