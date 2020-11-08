class solution:
    def isPalindrome(self,A):
        return 1 if str(A) == str(A)[::-1] else 0