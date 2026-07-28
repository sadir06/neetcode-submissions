from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = Counter(nums) 
        for keys, values in hashmap.items():
            if values > (len(nums) // 2):
                return keys