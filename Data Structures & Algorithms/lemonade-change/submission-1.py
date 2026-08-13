class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        Given a list of bills that need to be processed in order, each custormer pays 5$ and needs bills[i] - 5 dollars as change. In our change, we need to see if we can make change for all of them. Return True if possible, else False. 
        """
        current_change = defaultdict(int)
        
        for i, bill in enumerate(bills):
            if bill == 5:
                current_change[bill] = 1 + current_change.get(bill, 0)
            else:
                change = bill - 5
                current_change[bill] = 1 + current_change.get(bill, 0)
                if change in current_change and current_change[change] > 0: # this is the simple case where we just have a note of change
                    current_change[change] = current_change.get(change, 0) - 1
                    # We have paid them the change
                    continue
        
                if change == 15:
                    if current_change[5] >= 1 and current_change[10] >= 1:
                        current_change[5] -= 1
                        current_change[10] -= 1
                    elif current_change[5] >= 3:
                        current_change[5] -= 3
                    else:
                        return False
                elif change == 10:
                    if current_change[10] >= 1:
                        current_change[10] -= 1
                    elif current_change[5] >= 2:
                        current_change[5] -= 2
                    else:
                        return False
                else:
                    return False
        return True