class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n) :
            compliment = target - nums[i]
            if compliment in nums and nums.index(compliment) != i:
                return [nums.index(compliment),i]
            
            
        return []