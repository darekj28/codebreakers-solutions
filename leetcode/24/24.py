# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # base case
        if not head or not head.next:
            return head
        
        # create dummy to keep track of the head
        dummy = ListNode(1)
        dummy.next = head
        
        # instantiate variables for the loop
        prev = dummy
        curr = head
        next = head.next
        while curr and next:
            # store reference to the next iteration's curr
            nextCurr = next.next
            
            # flip the two nodes and connect them with the rest of the already swapped nodes
            prev.next = next
            next.next = curr
            curr.next = nextCurr
            
            # update for next iteration
            prev = curr
            curr = nextCurr
            if curr:
                next = curr.next
        return dummy.next