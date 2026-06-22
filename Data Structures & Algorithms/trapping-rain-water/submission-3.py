class Solution:
    def trap(self, height: List[int]) -> int:
        # OK we can start of by looking at each specific index, and determine how much water is trapped there based 

        n = len(height)
        total_volume = 0

        for i in range(n - 1):
            if i == 0:
                continue
            current_height = height[i]
            left, right = i - 1, i + 1
            max_left, max_right = 0, 0
            while left >= 0:
                max_left = max(max_left, height[left])
                left -= 1
            
            while right < n:
                max_right = max(max_right, height[right])
                right += 1

            tallest_wall = min(max_left, max_right) # This means that both walls have atleast the minimum water holding power
            if tallest_wall - current_height <= 0:
                continue
            total_volume += tallest_wall - current_height # Total volume get's added the current indexes water height - current block height. 
        
        return total_volume
        

