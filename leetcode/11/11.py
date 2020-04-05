class Solution:
    def maxArea(self, height: List[int]) -> int:
        # initialize variable to keep track of max volume
        maxVolume = 0
        # base cases for when max volume is 0
        if len(height) <= 1:
            return maxVolume
        
        leftIndex = 0
        rightIndex = len(height)-1
        while leftIndex < rightIndex:
            # the height is limited by the shorter wall
            currHeight = min(height[leftIndex], height[rightIndex])
            width = rightIndex - leftIndex
            maxVolume = max(maxVolume, currHeight*width)
            
            # update indices based on which index is limiting the height
            if height[leftIndex] < height[rightIndex]:
                leftIndex += 1
            else:
                rightIndex -= 1
        return maxVolume