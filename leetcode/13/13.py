class Solution:
    def romanToInt(self, s: str) -> int:
        # create map from roman string to int value
        symbolToValue = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        valueToReturn = 0
        # for each character in the input
        # if it precedes a larger number it is negative
        # and if it doesn't it's positive
        for i in range(len(s)):
            value = symbolToValue[s[i]]
            if i+1 < len(s):
                # the value of this roman character is negative
                if symbolToValue[s[i+1]] > value:
                    value *= -1
            valueToReturn += value
        return valueToReturn