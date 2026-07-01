# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None

        slow, fast = head, head

        while fast and fast.next: # We loop till we reach None and make sure to check that fast.next exsits and is NOT None, because we will do fast = fast.next.next
            slow = slow.next
            fast = fast.next.next
            
        # After this finishes running, slow is at the midpoint and fast is at the end of the list
        # Now we sever the connection creating 2 smaller linked lists. This is so that the first half doesn't bleed into the 2nd half when reversing
        head2 = slow.next
        slow.next = None

        current, prev = head2, None
        while current: 
            temp = current.next
            current.next = prev # Reverse
            prev = current
            current = temp # Move it along
        # Now head2 is completely reversed, meaning that we can start alternatively adding to the first list. Let's go!

        first, second = head, prev # We start at prev, rememnber that starts at the head of the newly reversed linked list
        while second: # The 2nd one is either always equal to or shorter than the first half
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1 # Make it point to the next value of the original first
            first = temp1
            second = temp2

        return