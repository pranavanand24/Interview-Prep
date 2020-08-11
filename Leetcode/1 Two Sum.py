class Solution:
    def twoSum(self, nums, target):

        seen = {}

        for index, num in enumerate(nums):
            other = target - num

            if other in seen:
                return [seen[other], index]
            else:
                seen[num] = index

        return []