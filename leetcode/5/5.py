class Solution:
    def longestPalindrome(self, s: str) -> str:
        # checking for empty inpu8t
        if len(s) == 0:
            return ""
        
        # initialize middle point to "fan out" from
        center_point = 0
        # keep track of our solution indices
        solIndices = [0,0]
        while center_point/2 < len(s):
            # if our palindrome is odd
            if center_point % 2 == 0:
                leftIndex = center_point//2
                rightIndex = leftIndex
            # if our palindrome is even
            else:
                leftIndex = center_point//2
                rightIndex = leftIndex + 1
            
            # while our string is a palindrome, update our starting and ending indices
            while leftIndex >= 0 and rightIndex < len(s) and s[leftIndex] == s[rightIndex]:
                # if the palindrome is longer than our previous solution, update it
                if rightIndex-leftIndex > solIndices[1]-solIndices[0]:
                    solIndices[1] = rightIndex
                    solIndices[0] = leftIndex
                leftIndex -= 1
                rightIndex += 1
            # update starting/center point for our palindrome
            center_point += 1
        
        return s[solIndices[0]:solIndices[1]+1]