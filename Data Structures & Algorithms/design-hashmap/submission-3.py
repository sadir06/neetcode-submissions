class ListNode:
    def __init__(self, key = -1, val = -1, next = None): # These values are hardcoded at creation, all you have to do to create a new object is ListNode()
        self.key = key
        self.val = val # We need this for the key : val corresponding data structure
        self.next = None

class MyHashMap:

    def __init__(self):
        self.store = [ListNode() for _ in range(1000)]     

    def hash(self, key: int) -> int:
        # Makes our lives a bit easier
        return key % len(self.store)

    def put(self, key: int, value: int) -> None:
        cur = self.store[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.store[self.hash(key)].next # We get the value of the next hash
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1
        

    def remove(self, key: int) -> None:
        cur= self.store[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)