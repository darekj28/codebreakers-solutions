class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # check for empty input
        if len(nums) == 0 :
            return 0
        
        # instantiate dp array
        # dp[i] represents length of longest increasing subsequence for nums[:i+1]
        dp = [0]*len(nums)
        dp[0] = 1
        
        # for each i, find the longest subsequence with all numbers less than nums[i] before it
        for i in range(1, len(nums)):
            longestSeq = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    longestSeq = max(longestSeq, dp[j])
            dp[i] = longestSeq + 1
        return max(dp)