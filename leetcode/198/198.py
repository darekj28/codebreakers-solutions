class Solution:
    def rob(self, nums: List[int]) -> int:
        # base cases
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # cached values for calculating the max we can steal up to the current house
        before = nums[0]
        prev = max(nums[0],nums[1])
        amountStealable = prev
        for i in range(2, len(nums)):
            # the most we can steal is based on two options:
            # if we steal from house i and if we don't and only steal from previous houses
            amountStealable = max(nums[i]+before, prev)
            # update dp variables
            before = prev
            prev = amountStealable
        return amountStealable