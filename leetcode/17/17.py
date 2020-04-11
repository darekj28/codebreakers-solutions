class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = []
        
        # check for empty string as input
        if len(digits) == 0:
            return combinations
        
        # dictionary to map from digit to possible characters
        digitToLetters = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        
        self._backtrack(combinations, digitToLetters, digits, 0, [])
        return combinations
    
    # backtrack through all possible combinations
    def _backtrack(self, combinations, digitToLetters, digits, i, charArray):
        # if we reach the end of our string, add the new combination of characters to our solution
        if i == len(digits):
            combinations.append("".join(charArray))
            return
        for char in digitToLetters[digits[i]]:
            # add new character
            charArray.append(char)
            # move on to next digit (dfs)
            self._backtrack(combinations, digitToLetters, digits, i+1, charArray)
            # backtrack
            charArray.pop()
        