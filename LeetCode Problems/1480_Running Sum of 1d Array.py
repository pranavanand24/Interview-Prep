class Solution:
    def runningSum(self, nums):
        result = []
        total = 0
        for i in range(len(nums)):
            total = total + nums[i]
            result.append(total)
        return result