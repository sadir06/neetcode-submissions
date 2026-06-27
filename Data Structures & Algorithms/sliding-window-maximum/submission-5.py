class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        temp = deque()
        left = 0

        for right in range(len(nums)):
            while temp and nums[right] > nums[temp[-1]]: # Temp stores the indices, not the numbers
                temp.pop()
            
            temp.append(right)
            
            if left > temp[0]: 
                temp.popleft()

            if right >= k - 1:
                output.append(nums[temp[0]])
                left += 1
        return output
