# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        current, prev = head, None # We start at the 2 directions of the list, the head, and the tail pointing at None

        while current: 
            nxt = current.next # Save the next value
            current.next = prev # Flips the polarity of the pointer, so the next value points to the previous value, 0 points to None, 1 points to 2, 2 to 3, and 3 becomes the head
            prev = current # I think this works, though we might have to go backwards
            current = nxt # We need to send it forward to the next one which is why we needed to remember it
            
        return prev

        