# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        dummy_right = ListNode()
        tail_right = dummy_right
        dummy_left = ListNode()
        tail_left = dummy_left

        curr = head

        while curr:
            if curr.val < x:
                tail_left.next = curr
                tail_left = curr
            else:
                tail_right.next = curr
                tail_right = curr
            curr = curr.next
        tail_left.next = dummy_right.next
        tail_right.next = None
        return dummy_left.next
        