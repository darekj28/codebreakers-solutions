class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        leftIndex = 0
        rightIndex = len(nums)-1
        while leftIndex <= rightIndex:
            middleIndex = leftIndex + (rightIndex-leftIndex)//2
            
            if nums[middleIndex] == target: 
                # we found our target!
                return middleIndex
            else:
                # if the left part of the search space is sorted
                if nums[leftIndex] <= nums[middleIndex]:
                    # if the target is in the sorted (left) portion of the array
                    if nums[leftIndex] <= target and target < nums[middleIndex]:
                        rightIndex = middleIndex - 1
                    # target is in the unsorted (right) portion of the array
                    else:
                        leftIndex = middleIndex + 1
                # the right part of the search space is sorted
                else:
                    # target is in the sorted (right) portion of the array
                    if nums[middleIndex] < target and target <= nums[rightIndex]:
                        leftIndex = middleIndex + 1
                    # target is in the unsorted (left) portion of the array
                    else:
                        rightIndex = middleIndex - 1
        # target not found in the array
        return -1
                    