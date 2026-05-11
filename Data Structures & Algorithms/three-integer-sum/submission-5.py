class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, num in enumerate(nums):

            if num > 0: # Remaining terms are positive as the list is sorted, and we cannot reach 0 anymore
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue # Another edge case, we cannot equal 0 here


            l, r = i + 1, len(nums) - 1
            while l < r:
                current_sum = num + nums[l] + nums[r]

                if current_sum > 0: # This means the right term is too large
                    r -= 1
                elif current_sum < 0:
                    l += 1
                else: # We have found a solution
                    result.append([num, nums[r], nums[l]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1]and l < r:
                        l += 1 # Extra case to find the terms faster, if l is the same as the previous l, and l < r, skip it
                    





        return result
            






        
