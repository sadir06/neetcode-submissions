# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy # We are ready to attach to whichever node is smallest, dummy.next will be returned as the actual head of our new linked list

        while list1 and list2: # We break if atleast 1 reaches None, and then at the end we will just add on the rest of the terms by checking if list1 or if list2
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        while list1:
            current.next = list1
            list1 = list1.next
            current = current.next
        while list2:
            current.next = list2
            list2 = list2.next
            current = current.next

        return dummy.next # Current is now at the end of our linked list

