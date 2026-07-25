class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n > 1:
            temp = x
            for i in range(n - 1):
                x = x * temp
            return x
        if n == -1:
            return 1/x
        if n < - 1:
            temp = x
            for i in range((-n) + 1):
                x = x / temp
            return x