class Solution:
    def myAtoi(self, str: str) -> int:
        # check for empty string
        if len(str) == 0:
            return 0
        
        # skip all white spaces
        i = 0
        while i < len(str) and str[i] == " ":
            i += 1
    
        # get the sign of the number
        sign = 1
        if i < len(str) and (str[i] == "+" or str[i] == "-"):
            if str[i] == "-":
                sign *= -1
            i += 1
        
        # check to make sure we haven't reached the end of the string
        if i == len(str):
            return 0
        
        # get all the valid numeric digits of our integer
        stringbuffer = []
        while i < len(str) and str[i].isnumeric():
            stringbuffer.append(str[i])
            i += 1
            
        # check that there are valid digits in our string
        if len(stringbuffer) == 0:
            return 0
        
        # cast our string to an integer
        myInt = int("".join(stringbuffer))*sign
        
        # check bounds
        if myInt < -2**31:
            return -2**31
        if myInt > 2**31-1:
            return 2**31-1
        
        return myInt