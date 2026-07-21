class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set() # Helps with duplicates
        nums.sort()
        for i, num in enumerate(nums):
            left, right = i + 1, len(nums) - 1

            while left < right:
                if num + nums[left] + nums[right] == 0:
                    output.add((num, nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif num + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1


        return list(output)