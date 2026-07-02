# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        dummy = ListNode(0) # Create a dummy Linked list with value 0, and no next
        dummy.next = head
        current = dummy
        
        steps_to_move = length - n # Lenght - n is how many steps we move up the linked lists
        for _ in range(steps_to_move):
            current = current.next

        current.next = current.next.next

        return dummy.next