class Solution:
    def longestMountain(self, A: List[int]) -> int:
        longestLength = 0
        # a mountain has a minimum length of 3
        if len(A) < 3:
            return 0
        
        lIdx = 0
        while lIdx < len(A):
            # initialize the end of the mountain
            rIdx = lIdx
            
            # find peak of mountain
            while rIdx + 1 < len(A) and A[rIdx+1]>A[rIdx]:
                rIdx += 1
            
            # there is no increasing (left) side of the mountain
            if rIdx == lIdx:
                # the next potential mountain starts in the next index
                lIdx += 1
                continue
            
            peakIdx = rIdx
            # find the bottom right of the mountain
            while rIdx + 1 < len(A) and A[rIdx+1]<A[rIdx]:
                rIdx += 1
            
            # there is no decreasing (right) side of the mountain
            if rIdx == peakIdx:
                # the next potential mountain starts in the next index
                lIdx = rIdx + 1
                continue
            
            # update the length of the longest mountain we've found so far
            longestLength = max(longestLength, rIdx-lIdx+1)
            
            # the next potential mountain can start at the end of the current mountain
            lIdx = rIdx
        return longestLength