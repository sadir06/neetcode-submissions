from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return [nums[0]]
        output = []
        store = Counter(nums)
        for num, count in store.items():
            if count > (n // 3):
                output.append(num)
        return output