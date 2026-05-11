class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i:
                    continue
                else:
                    output[i] *= nums[j] 
        return output