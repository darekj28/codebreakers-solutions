class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # make a string that's the reverse of s
        reverseS = collections.deque()
        for char in s:
            reverseS.appendleft(char)
        reverseS = "".join(reverseS)
        
        # find longest common substring of s and reverseS is a palindrome!
        # use dp to get the LCS(s, reverseS)
        
        dpMatrix = [[0 for i in range(len(s)+1)] for j in range(len(s) + 1)]
        for r in range(1, len(s) + 1):
            for c in range(1, len(s) + 1):
                # if the current characters are the same, then
                if s[r-1] == reverseS[c-1]:
                    # it reduces to LPS(s[:r], reverseS[:c]) + 1
                    dpMatrix[r][c] = dpMatrix[r-1][c-1] + 1
                else:
                    # it reduces to max(LPS(s[:r-1],reverseS[:c]), LPS(s[:r],reverseS[:c-1]))
                    dpMatrix[r][c] = max(dpMatrix[r-1][c], dpMatrix[r][c-1])
                    
        return dpMatrix[-1][-1]