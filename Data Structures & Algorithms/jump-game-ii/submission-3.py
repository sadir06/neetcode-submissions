class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jumps = 0
        current_end = 0
        farthest = 0
        for i in range(len(nums) - 1): # Game is over once we land on the final one, we don't need to jump from it
            farthest = max(farthest, i + nums[i]) # Absolute farthest we can jump from this inedx
            if farthest >= len(nums) - 1:
                return min_jumps + 1
            
            if i == current_end:
                min_jumps += 1
                current_end = farthest
            # Else, we just keep going to the next index looking for the current end. We do this so that we can search all opportunities to see if we can find a better point

        return min_jumps