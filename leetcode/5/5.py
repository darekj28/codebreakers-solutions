class Solution:
    def longestPalindrome(self, s: str) -> str:
        # checking for empty inpu8t
        if len(s) == 0:
            return ""
        
        # initialize middle point to "fan out" from
        center_point = 0
        # keep track of our solution indices
        solIdx = [0,0]
        while center_point/2 < len(s):
            # if our palindrome is odd
            if center_point % 2 == 0:
                lIdx = center_point//2
                rIdx = lIdx
            # if our palindrome is even
            else:
                lIdx = center_point//2
                rIdx = lIdx + 1
            
            # while our string is a palindrome, update our starting and ending indices
            while lIdx >= 0 and rIdx < len(s) and s[lIdx] == s[rIdx]:
                # if the palindrome is longer than our previous solution, update it
                if rIdx-lIdx > solIdx[1]-solIdx[0]:
                    solIdx[1] = rIdx
                    solIdx[0] = lIdx
                lIdx -= 1
                rIdx += 1
            # update starting/center point for our palindrome
            center_point += 1
        
        return s[solIdx[0]:solIdx[1]+1]