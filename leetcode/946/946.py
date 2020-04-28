class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # initiate variable for popped index
        i = 0
        
        # create stack to emulate pushing and popping
        currStack = []
        for num in pushed:
            currStack.append(num)
            # pop as many values as we can from currStack
            while currStack and i < len(popped) and currStack[-1] == popped[i]:
                currStack.pop()
                i += 1
                
        return len(currStack) == 0
                