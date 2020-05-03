class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self._isPalindrome(s, 0, len(s)-1, False)
    
    # moves outwards to inwards to check if the string is a valid palindrome
    def _isPalindrome(self, s, leftIndex, rightIndex, hasDeleted):
        while leftIndex < rightIndex:
            # move inwards
            if s[leftIndex] == s[rightIndex]:
                leftIndex += 1
                rightIndex -= 1
            else:
                # if we already deleted a character, return False
                if hasDeleted:
                    return False
                # check if the palindrome is valid if we delete each of the current characters
                return self._isPalindrome(s, leftIndex+1, rightIndex, True) or self._isPalindrome(s, leftIndex, rightIndex-1, True)
        return True