class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        output = []

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for _ in range(k):
            max_key =  max(count, key=count.get)
            output.append(max_key) # we append the keys and not the frequency values
            count.pop(max_key)

        return output