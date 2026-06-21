class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        outputs = set()
        if len(nums) <= 2:
            return "You are a dumbass, this question is dumb and wrong"
        nums.sort() # This will be usedful to use pointers
        n = len(nums)
        for i in range(n - 2): # This new method doesn't require us to look at the last 2 terms, because ther are no more left and right terms to deal with
            left, right = i + 1, n - 1 # index start to end from A
            while left < right: # Again we can't have <= because we need 2 more distint numbers
                if nums[i] + nums[left] + nums[right] == 0:
                    temp = [nums[i], nums[left], nums[right]] # This is automatically sorted because we sorted it initially, and we keep going here. 
                    outputs.add(tuple(temp))
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
        output = list(outputs) # forgive the naming scheme lol

        return output

