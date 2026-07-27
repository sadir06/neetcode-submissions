class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashset = set()
        for i in range(0, len(nums)):
            hashset.add(nums[i])
        max_num = max(nums)
        print(hashset)
        for i in range(0, max_num):
            if i not in hashset:
                return i
        return max_num + 1