class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        We are given a positive integer num, we have to return true if nuum is a perfect square else we return false. A perfect quare is just an integer that is hte square of another integer, e.g. 16 is a true square. While we can just use a built in sqrt function, that's actually not allowed. So instead what we can do is do a binary search from 1 to num // 2 to check if the square of any of the numbers squared is equal to num. Simple. Else we return False.
        """
        if num == 1:
            return True
             
        left, right = 1, num // 2
        while left <= right:
            mid = (left + (right - left) // 2)
            square = mid * mid
            if square == num:
                return True
            elif square > num:
                right = mid - 1
            else:
                left = mid + 1
        return False