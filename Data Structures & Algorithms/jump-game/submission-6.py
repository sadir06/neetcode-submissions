class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1 # Set it to the final index we need to reach
        for i in range(len(nums) - 1, -1, -1): # we loop till the first index, backward
            if i + nums[i] >= goal: # We are guareented to reach the end if we can reach this new point, this becomes our new goal
                goal = i  # We set our new goal to reach this new index, because we know that if we reach it, we can win by going to the end. 
        
        return goal == 0
