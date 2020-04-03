class Solution:
    '''
    Time Complexity: O(len(A) + len(B)), linear to the input since we have to go through all the elements in both arrays to get all the intersections
    Space Complexity: O(max(len(A), len(B))) since the max number of intersections is the length of the longer of the two lists.
    '''
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        # instantiate solutions array and check for empty inputs
        intersection = []
        if len(A) == 0:
            return intersection
        if len(B) == 0:
            return intersection
        
        aIndex = 0
        bIndex = 0
        while aIndex < len(A) and bIndex < len(B):
            aStart = A[aIndex][0]
            aEnd = A[aIndex][1]
            bStart = B[bIndex][0]
            bEnd = B[bIndex][1]
            
            # if the two interals intersect, it will begin at the larger of the two
            # starting points and end at the smaller of the two endpoints
            potentialStart = max(aStart, bStart)
            potentialEnd = min(aEnd, bEnd)
            # if there's an intersection, add it to our intersections list
            if potentialStart <= potentialEnd:
                intersection.append([potentialStart, potentialEnd])
            
            # increment the interval that ends first
            if aEnd <= bEnd:
                aIndex += 1
            else:
                bIndex += 1
                
        return intersection
                
            
        
