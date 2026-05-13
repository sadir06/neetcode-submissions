class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)

            current_sum = 0
            for digit in str(n):
                current_sum += int(digit) ** 2
            
            n = current_sum
        
        return n == 1