class Solution:
      def fizzBuzz(self, A):
        l = []
        for i in range(1, A+1):
            if i % 15 == 0:
                l.append("FizzBuzz")
            elif i % 3 == 0:
                l.append("Fizz")
            elif i % 5 == 0:
                l.append("Buzz")
            else:
                l.append(i)
        return l
    