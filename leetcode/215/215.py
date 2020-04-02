class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self._quickselect(nums, 0, len(nums)-1, k)
    
    def _quickselect(self, nums, leftIndex, rightIndex, k):
        pivotIndex = random.randint(leftIndex, rightIndex)
        partitionIndex = self._partition(nums, leftIndex, rightIndex, pivotIndex)
        
        if partitionIndex == len(nums)-k: # if we've found the kth largest
            return nums[partitionIndex]
        elif partitionIndex > len(nums)-k:
            return self._quickselect(nums, leftIndex, partitionIndex-1, k)
        else:
            return self._quickselect(nums, partitionIndex+1, rightIndex, k)
    
    def _partition(self, nums, leftIndex, rightIndex, pivotIndex):
        pivotValue = nums[pivotIndex]
        # move pivot out of the way as we partition the array
        self._swap(nums, pivotIndex, rightIndex)
        # move all values smaller than the pivot to the left
        for i in range(leftIndex, rightIndex):
            if nums[i] < pivotValue:
                self._swap(nums, leftIndex, i)
                leftIndex += 1
        # move pivot back to its proper place in the array
        self._swap(nums, leftIndex, rightIndex)
        return leftIndex
    
    # helper function to swap two indices in an array
    def _swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp