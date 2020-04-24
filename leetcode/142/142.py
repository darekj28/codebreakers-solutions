# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # check to see if head is None or of length 1
        if not head or not head.next:
            return None
        
        # use 2 pointers to find if there's a cycle
        slow = head.next
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # cycle found
            if slow == fast:
                break
        
        # there's no cycle if they don't equal each other
        if slow != fast:
            return None
        
        # move one of the nodes to the head of the list, then
        # increment the two pointers one at a time and when they meet again
        # we've found the start of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow