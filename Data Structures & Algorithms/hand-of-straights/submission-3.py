class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        n  = int(len(hand) / groupSize)
        hand.sort()
        count = Counter(hand) # Creates a frequency map that we can use

        for card in hand:
            if count[card] == 0:
                continue # We can't use this card
            for i in range(groupSize):
                if count[card + i] <= 0:
                    return False # We have hit the case, we can't create n sublists
                count[card + i] -= 1
        return True