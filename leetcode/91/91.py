class Solution:
    def numDecodings(self, s: str) -> int:
        
        # deal with base cases and initialize dp data
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        if len(s) == 2:
            if s == "10" or s == "20":
                return 1
        
        numWays = [1]*2 # represents [numways(s[:i-2]), numways(s[:i-1])]    
        if s[1:2] == "0":
            numWays[1] = 0
        if int(s[:2]) <= 26:
            numWays[1] += numWays[0]
        
        for i in range(2, len(s)):
            singleDigitNum = int(s[i])
            doubleDigitNum = int(s[i-1:i+1])
            
            # if the current digit leads to a new character being decoded
            nextNumWays = 0
            if singleDigitNum > 0:
                nextNumWays += numWays[1]
            # if the last two digits lead to a new character being decoded
            if doubleDigitNum > 9 and doubleDigitNum <= 26:
                nextNumWays += numWays[0]
            
            # update dp data
            numWays[0] = numWays[1]
            numWays[1] = nextNumWays
        return numWays[-1]