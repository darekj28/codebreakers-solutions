class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ensure the input isn't empty
        if s == "":
            return True
        # ensure that there are no upper case characters for consitency
        s = s.lower()
        leftIndex = 0
        rightIndex = len(s)-1
        while leftIndex < rightIndex:
            # ignore non alphanumeric values
            if not s[leftIndex].isalnum():
                leftIndex += 1
                continue
            if not s[rightIndex].isalnum():
                rightIndex -= 1
                continue
            # if the values are the same, we continue iterating through the string
            if s[leftIndex] == s[rightIndex]:
                leftIndex += 1
                rightIndex -= 1
            # we're not a palindrome and return False
            else:
                return False
        # if we go through the whole string, the string is a palindrome
        return True