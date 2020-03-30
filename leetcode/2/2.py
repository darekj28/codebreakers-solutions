# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


"""
Motivation:
Since the list is already ordered so the least significant digits come first, (the ones digits are
the head, the head points to the tens digits, the tens digits point to the hundreds digits, etc) a 
straightforward strategy is to just loop through both lists 1 node at a time and sum them to find 
the value of our solution's corresponding node for that digit. (Taking the list 1->9->2 to 
represent 291 and 4->4->4 as 444 for example, to get the 1's digit for our solution, we merely need
to sum 1 and 4 to get 5.) If the sum of the two node values exceed 9, then we must only use the the
1's digit in the sum and store the remainder for the next pair of nodes to be summed. 

Time Complexity:
The time complexity is linear in the number of nodes in the longer list, since we have to go
through each digit.

Space Complexity:
The space complexity is O(max(length of l1, length of l2)). The most nodes you'll ever make is the
number of digits in the longer list + 2 (1 for the dummy head and 1 if there's an extra remainder
from the sum).
"""

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # we create a dummy node to point that points to the solution's head to return at the end
        dummy = ListNode(None)

        # we keep track of the last node created which will point to the next node we create
        last = dummy
        remainder = 0 # the remainder defaults to 0 when summing the 1's digits
        while l1 or l2:
            # we calculate the value of the new node to be created
            currVal = remainder
            # we must check if the nodes are null for the case that one of the lists is longer
            if l1:
                currVal += l1.val
                l1 = l1.next
            if l2:
                currVal += l2.val
                l2 = l2.next

            # if the value of the new node is 10 or greater, then we must store the remainder and 
            # update the value to be stored in the new node
            remainder = currVal // 10
            currVal %= 10
            currNode = ListNode(currVal)
            # we connect the solution we are building with the newly created node
            last.next = currNode
            last = currNode
        # if there is still a remainder after going through both lists, we need to add it to the
        # list. Take 8->8->8 and 2->4->7 as an example.
        if remainder:
            currNode = ListNode(remainder)
            last.next = currNode
        return dummy.next