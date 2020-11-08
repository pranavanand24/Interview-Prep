class Solution:
    def reverse(self, A):
        B = abs(A)
        a = list(str(B))
        a.reverse()
        c = ""
        c = int(c.join(a))
        if c > 2 ** 31:
            return 0
        else:
            if A >= 0:
                return c
            else:
                return -c