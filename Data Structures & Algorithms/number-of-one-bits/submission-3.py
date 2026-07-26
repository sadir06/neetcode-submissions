class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            n = n & (n - 1) # Every time we subtract, we remove 1 bit and increment
            count += 1
        return count
