class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums) #This line does all the counting for me!
        buckets = [[] for _ in range (len(nums) + 1)]
        result = []
        for num, freq in counts.items():
            buckets[freq].append(num)
        for i in range(len(buckets) - 1, 0, -1):
            
            if len(result) == k:
                break
            else: 
                result.extend(buckets[i]) 
        return result
