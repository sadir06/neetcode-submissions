class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = max(nums)
        store = [0] * (n + 1) 
        for num in nums:
            store[num] += 1
        return store.index(max(store))
