class Solution:
    def longestMountain(self, A: List[int]) -> int:
        longestLength = 0
        # a mountain has a minimum length of 3
        if len(A) < 3:
            return 0
        
        mtd_start = 0
        while mtd_start < len(A):
            # initialize the end of the mountain
            mtd_end = mtd_start
            
            # find peak of mountain
            while mtd_end + 1 < len(A) and A[mtd_end+1]>A[mtd_end]:
                mtd_end += 1
            
            # there is no increasing (left) side of the mountain
            if mtd_end == mtd_start:
                # the next potential mountain starts in the next index
                mtd_start += 1
                continue
            
            peakIdx = mtd_end
            # find the bottom right of the mountain
            while mtd_end + 1 < len(A) and A[mtd_end+1]<A[mtd_end]:
                mtd_end += 1
            
            # there is no decreasing (right) side of the mountain
            if mtd_end == peakIdx:
                # the next potential mountain starts in the next index
                mtd_start = mtd_end + 1
                continue
            
            # update the length of the longest mountain we've found so far
            longestLength = max(longestLength, mtd_end mtd_start+1)
            
            # the next potential mountain can start at the end of the current mountain
            mtd_start = mtd_end
        return longestLength