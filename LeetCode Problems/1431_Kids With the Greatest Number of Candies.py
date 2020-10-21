class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maxcandies = max(candies)
        result = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxcandies:
                result.append(True)
            else:
                result.append(False)
        return result