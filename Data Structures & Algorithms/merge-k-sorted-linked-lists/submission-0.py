# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeTwoLists(self, list1, list2): # This takes in the 2 competing sorted lists, and creates a new list to return that is the winner, in other words which is sorted
        if list2 is None: # This means that this one didn't get a pairing as we had an odd number and this one was at the end
            return list1 # The winner is just the only list that we have
        dummy = ListNode()
        current = dummy 
        while list1 and list2: # While we don't reach None in the longer list
            if list1.val >= list2.val:
                 current.next = list2
                 list2 = list2.next
            else: 
                current.next = list1
                list1 = list1.next
            current = current.next

        current.next = list1 or list2 # Tack on the remaining list

        return dummy.next # Remember that this is the head

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        # OK so previously, when we had merge 2 linked lists, we did this by taking the 2 lists, and alternating between then based on the smallest value. However, we can't do this here because we could have hundereds of lists and we can't just have variables for all of those. So we need a way to loop through all of the linked list. 
        # Ok so given an array of linked lists (so we need to do something like lists[1].next in order to be able to get the values of those lists) We return a sorted linked list. 
        
        # We will have a tournament of lists, pairing them up and then merging them togethetr, until we have only 1 list left
        while len(lists) > 1:
            merged_list = [] # This is a temporary list where we will hold the winners and replace in lists. 
            for i in range(0, len(lists), 2):
                l1 = lists[i]

                l2 = lists[i + 1] if (i + 1) < len(lists) else None

                winner = self.mergeTwoLists(l1, l2)

                merged_list.append(winner)
            lists = merged_list # We overwrite the old array with the winners each round until we only have 1 remaining winner, fully sorted list

        return lists[0] # The only list that will exist in lists at the end is the linked lists that we will require