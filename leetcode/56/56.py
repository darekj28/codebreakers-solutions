class Solution:
    '''
    Time complexity: O(nlog(n)) since we sort the array.
    Space complexity: `O(n)` to construct the mergedIntervals array.
    '''
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        # ensure that the input is sorted
        intervals.sort()
        
        # initialize solution
        mergedIntervals = [intervals[0]]
        
        # add intervals or merge them into the previous interval
        for i in range(1, len(intervals)):
            currInterval = intervals[i]
            # if there's an intersection
            if currInterval[0] <= mergedIntervals[-1][1]:
                # if the current interval is ends after the previous interval
                if currInterval[1] > mergedIntervals[-1][1]:
                    mergedIntervals[-1][1] = currInterval[1]
            else:
                mergedIntervals.append(currInterval)
                
        return mergedIntervals