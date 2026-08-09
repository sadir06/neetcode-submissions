class Solution:
    def order_checker(self, order, a, b):
        # Returns true if char a comes before char b in the alpabet, a and b cannot be the same
        l, r = 0, len(order) - 1
        while order[l] != a:
            l += 1
        while order[r] != b:
            r -= 1
        if l > r: # this means that b is greater than a and should be first, return False
            return False
        else:
            return True
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words) - 1):
            word_a = words[i]
            word_b = words[i + 1]
            n = min(len(word_a), len(word_b))

            for j in range(n):
                if word_a[j] == word_b[j]:
                    continue
                if self.order_checker(order, word_a[j], word_b[j]):
                    break # break this inner loop and move to the next pair of words
                else:
                    return False
            else:
                if len(word_a) > len(word_b):
                    return False # If the first word is longer, it's out of order

        return True # if all checks survive