"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        dummy = Node(0)
        current_new = dummy
        current_old = head
        map = {}

        while current_old:
            current_new.next = Node(current_old.val)
            current_new = current_new.next
            map[current_old] = current_new
            current_old = current_old.next
            


        current_old = head
        current_new = dummy.next
        while current_old:
            map[current_old].random = map.get(current_old.random) # This uses the correct .get(), so we get the actual old node instead of pointing directly to it, and also it avoids the error of trying to access a possible None 
            current_new = current_new.next
            current_old = current_old.next

        return dummy.next