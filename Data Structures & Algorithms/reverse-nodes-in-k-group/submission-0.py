# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def helper(self, current, k):
        while current and k > 0:
            current = current.next
            k -= 1
        return current

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy # This is so that we can keep track of the original head that we have to return
        while True:
            output = (self.helper(groupPrev, k)) # This stores the next of the current list, so that we can restore it when trying to find the next linked list, should be None at the very final linked lists, so that the curernt list encompasses all elements
            if not output:
                break
            groupNext = output.next

            prev = groupNext
            current = groupPrev.next
            # The current group is head -> output, so we know that we need to reverse everything inbetween
            while current != groupNext:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            temp = groupPrev.next

            groupPrev.next = output

            groupPrev = temp



        return dummy.next