class Solution:
    def reverse(self, x: int) -> int:
        new_int, negative = 0, False
        max_val = 2147483647
        if x < 0:
            negative = True
            x = -x
        while x:
            new_int = (new_int * 10) + x % 10 # this is an excellent way to construct reverse integers as we take the modulo to carry the final number, and we multiply the other number by 10 to increase it's position before adding this new number, and floor division eliminates if from the other number
            x = x // 10
        print(max_val)
        if not negative and new_int > max_val - 1:
            return 0
        if negative and new_int > max_val:
            return 0
        if negative:
            new_int = - new_int
        
        return new_int
