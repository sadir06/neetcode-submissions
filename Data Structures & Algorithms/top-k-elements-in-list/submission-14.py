class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)] # Create a sublist

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num, frequencies in count.items():
            freq[frequencies].append(num) # Don't replace the sublist, append to it
        
        res = []
        for i in range(len(freq) - 1, 0, -1): # Loop in reverse so that you get the largest frequencies first
            for num in freq[i]:
                res.append(num) # Append all values if multiple values have the same really high frequency
                if len(res) == k:
                    return res

        

            

