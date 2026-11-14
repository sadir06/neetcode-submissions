class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        We are given an integer array nums sorted in ascending order. Return an array of the squares of each number sorted in non decreasing order. this might seem like the easiest question ever because we can literally just do a one pass, but then you see we have negative numbers too. Then you might think ok, we can just turn everything positive, or square everything and then resort it, right? Well that works but it is too slow (O(nlogn)). We can definitely do an O(n) since we already know that the list is sorted. SO what can we do instead? Let's look at the first example. We can see some sort of pattern. Looking at the opposites, we can clearly see that first we have -4 and 10. Comparing absolute values we can just pick 10 first. Then we can move that up and see that abs(-4) > 3, so we pick 4 and increment that. And we keep doing that until left == right. Then we return the reverse of hte array. We also make sure to square before adding to the output. 
        """
        output = []
        left, right = 0, len(nums) - 1 # We know that len(nums) is atleast 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                output.append(abs(nums[left]) ** 2)
                left += 1
            else:
                output.append(abs(nums[right]) ** 2)
                right -= 1
        
        return output[::-1]