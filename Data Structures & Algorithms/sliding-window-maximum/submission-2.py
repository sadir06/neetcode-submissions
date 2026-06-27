class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        left, right = 0, k - 1 # Window always starts here
        temp = deque() # Construct this for now, and we can basically append the next right and cut off the left every time

        while right < len(nums):
            if not temp: # We only do this the first time, as it won't be empty after appending
                for i in range(k):
                    temp.append(nums[i]) # Add the first few numbers into the initial sublist

            output.append(max(temp)) # O(K) we can find a way of making this faster by keeping the current biggest so far and seeing if the new number is bigger than the latest number that is still in the sublist
            left += 1
            right += 1 # We do this here because at the end of the loop the list moves up
            temp.popleft() # Remove the leftmost item we have moved on
            if right == len(nums):
                break
            temp.append(nums[right])

        return output