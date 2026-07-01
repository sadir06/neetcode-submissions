# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow, fast = head, head.next

        while slow and fast: # If either ever go to None, then there is no cycle and we instantly return false
            if slow == fast:
                return True # If at any point they are at the same point, there MUST have been a cycle
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next


        
        return False