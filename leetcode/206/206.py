# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


"""
Note: I highly recommend the iterative approach since it is more intuitive, efficient, and easier
to code. The recursive solution is provided merely for those who wish to practice and familiarize 
themselves further with recursion.

Iterative Approach:
Motivation:
For the purposes of explanation, assume we have the list: A -> B -> C -> None
To reverse any node, take B as an example, in the linked list, we need access to both the node
whose pointer will be reversed (B), the previous node (A), and the node after it (C). Why do we 
need a variable with access to C? Well, once we set B's next pointer to A (B.next = A), we no 
longer have a way to access node C! The work around is to store C in a temp variable before 
changing B's next pointer. To approach this problem, we keep track of 3 variables (prev, curr, 
and next) as we move through the linked list and reverse the next pointers.

Time Complexity:
We visit each node once, leading to a time complexity of O(n), linear in the number of nodes. 

Space Complexity:
We always use a constant number of pointers, leading to a space complexity of O(1).




Recursive Approach: 
Motivation:
Recursion allows us to work backwards once the base case is hit and the call stack begins to 
"unwind". We can take advantage of this to keep track of the new head of the reversed list, 
allowing us to avoid storing the current node's next node in a temporary pointer. 

Time Complexity:
We visit each node once, leading to a time complexity of O(n), linear in the number of nodes. 

Space Complexity:
The recursive call stack grows until we hit our base case (the end of the list), leading to a space
complexity of O(N).
"""

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # base case, there's nothing to reverse
        if not head or not head.next:
            return head
        
        prev = None # the current head will point to None once the list is reversed
        curr = head # curr represents the node whose next pointer will "change direction"
        while curr:
            next = curr.next # save a reference to the node next in the original linked list
            curr.next = prev # point curr to the previous node
            prev = curr # update the head of the reversed list
            curr = next # update curr to the next node whose pointer needs to change
        return prev 


# note that the function signature has been altered to avoid confusing variable names
class Solution:
    def reverseList(self, currNode: ListNode) -> ListNode:
        # base case, there's nothing to reverse
        if currNode is None or currNode.next is None:
            return currNode 
        # when we reach the base case, we'll return the new head of the list
        newHead = self.reverseList(currNode.next)
        # take the node originally after the current node and point it to itself
        currNode.next.next = currNode 
        # we have to set the current node's next pointer to None for when the recursion ends
        currNode.next = None 
        return newHead
