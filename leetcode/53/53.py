class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # handle empty input case
        if len(nums) == 0:
            return 0
        # keep track of the running sum of the previous index
        prev = nums[0]
        # keep track of the running max
        maxSum = prev
        # loop through rest of the array
        for i in range(1, len(nums)):
            # the maximum subarray sum for all cells up to index i in the array is either the value in the cell itself, 
            # or the current value + the previous subarray's sum
            curr = max(nums[i]+prev, nums[i])
            maxSum = max(maxSum, curr)
            prev = curr
        return maxSum