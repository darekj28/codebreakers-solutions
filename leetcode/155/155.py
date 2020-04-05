class MinStack:
    # all methods and initialization of this data structure run in constant time and memory
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.numStack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.numStack.append(x)
        # if the number being pushed is our new minimum, push it to the min stack
        if not self.minStack or self.minStack[-1] >= x:
            self.minStack.append(x)

    def pop(self) -> None:
        toReturn = self.numStack.pop()
        # if the top of our minStack matches the value to be popped, we must pop it off the minStack as well
        if toReturn == self.minStack[-1]:
            self.minStack.pop()
        return toReturn

    def top(self) -> int:
        return self.numStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()