class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.store = [ListNode(0) for _ in range(10**4)] # Initialise an array of 10000 buckers, each with a dummy head node, and the hsah key will be key % 10000 -> Gives us a solid range of 10000 values where each one will be unique, giving us a nice hash space.

    def add(self, key: int) -> None:
        cur = self.store[key % len(self.store)] # This is our hash that is generated
        while cur.next: 
            if cur.next.key == key:
                return # This just checks for duplicates, as if the key already exists, we don't add anything
            cur = cur.next # Check the entire linked list
        cur.next = ListNode(key) # If the check is passed, then we add the value at the specified hash by creating a new node with value key.         

    def remove(self, key: int) -> None:
        cur = self.store[key % len(self.store)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next # We skip over the value by having the pointer point to the next value instead! Since the key value will have no more references to it, the reference counter will clean this up
                return
            cur = cur.next
        # If the value is not in our data structure, we just exit without doing anyhting
    def contains(self, key: int) -> bool: # This is an O(1) implemention of the "in" checker keyword
        cur = self.store[key % len(self.store)] # we could hardcode this to 10000, but this is better
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)