class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1 # Set the goal to the final index

        for i in range(len(nums) - 2, -1, -1): # Loop backwards, from the 2nd last term, to the first term (-1 because that end of the for loop is exclusive)
            if i + nums[i] >= goal: # If from index i, we can jump to the current goal, or beyond, then index i becomes the new goal
                goal = i # i becomes the new goal that we need to set

        return goal == 0 # When we reach the first index, if goal == 0 (which would be the first index), then we return true

