class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range((len(nums) + 1))] # The frequency of a number cannot be larger than n, obviously, so at each position, we can put a number at it's frequency spot

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)

        for key, value in count.items():
            freq[value].append(key)

        output = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                output.append(num)
                k -= 1
                if k == 0:
                    return output


        

            

