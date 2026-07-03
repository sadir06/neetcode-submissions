# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_store, l2_store = [], []
        
        while l1:
            l1_store.append(l1.val)
            l1 = l1.next
        while l2: 
            l2_store.append(l2.val)
            l2 = l2.next

        number1, number2 = int("".join(map(str, reversed(l1_store)))), int("".join(map(str, reversed(l2_store))))

        result = number1 + number2

        result_list = [int(digit) for digit in reversed(str(result))]

        dummy = ListNode(0)
        current = dummy
        for digit in result_list:
            current.next = ListNode(digit) # We have to create the full node, and we do it by instantiating a new object for the digit as the input
            current = current.next
        return dummy.next