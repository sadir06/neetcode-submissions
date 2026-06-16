class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 4, 6]
        res = [1] * len(nums)
        # [1, 1, 1, 1]
        prefix = 1

        for i, num in enumerate(nums):
            res[i] = prefix
            prefix *= num
            # [1, 1, 2, 8]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1): # Loop in reverse
            res[i] *= postfix
            postfix *= nums[i]
            # [48, 24, 12, 8]
    
        return res

            