# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = None, head

        while current:
            temporary = current.next #Assign the next value of head to temp
            current.next = previous #Set the next value as the previous value (reverse it)
            previous = current # Set the previous value as the current value (swaping the elements), as previous is the reversed linked list that we are building, we don't care what happens to current
            current = temporary # Set the current value to be next value and loop again
        return previous # Starts as none, and obtains all the elements in current but reverse
    