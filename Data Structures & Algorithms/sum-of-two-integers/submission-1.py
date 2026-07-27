class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b != 0:
            carry = (a&b) << 1
            a = (a ^ b) & mask # Mask simulates 32-bit unsigned integers
            b = carry

        return a if a < 0x7FFFFFFF else ~(a ^ mask) # 2s complement