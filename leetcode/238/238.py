class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = [None] * len(nums)
        # store running products from left to right in our output array
        runningProduct = 1
        for i in range(len(nums)):
            runningProduct *= nums[i]
            sol[i] = runningProduct
        # keep track of running product from right to left and update the output array
        runningProduct = 1
        for i in reversed(range(len(nums))):
            # check out of bounds error before updating the running product from the right
            if i+1 < len(nums):
                runningProduct *= nums[i+1]
            
            # calculate the product without the element nums[i]
            sol[i] = runningProduct
            if i-1 >= 0:
                sol[i] *= sol[i-1]
        return sol