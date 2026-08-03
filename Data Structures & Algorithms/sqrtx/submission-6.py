class Solution:
    def mySqrt(self, x: int) -> int:
        k = (x // 2) + 2

        for i in range(k):
            if i * i == x:
                return i
            elif i * i > x: # This one went just above, rounded down, it would be i - 1
                return i - 1
        if x == 0:
            return 0
        if x == 1:
            return 1
        if x == 2:
            return 1