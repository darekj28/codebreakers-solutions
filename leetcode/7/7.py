class Solution:
    def reverse(self, x: int) -> int:
        # keep track of integer sign
        isPositive = x >= 0
        # char queue as a string builder
        newNumber = collections.deque()
        
        for char in str(abs(x)):
            # update sign if necessary
            newNumber.appendleft(char)
        
        # add sign to our string bugger
        if not isPositive:
            newNumber.appendleft("-")
        
        # create our new number
        newNumber = int("".join(newNumber))
        
        # check if our number is outside the 32 bit signed integer range
        if newNumber < -2**31 or newNumber > 2**31-1:
            return 0
        
        return newNumber