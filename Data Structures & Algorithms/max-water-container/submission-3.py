class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_volume = 0
        while left < right: # Not <= because the same bar cannot hold in any water, obviously
            lh = heights[left]
            rh = heights[right]
            water_height = min(lh, rh) # You can only hold in as much water as the shortest bar
            water_width = right - left 
            max_volume = max(max_volume, water_height * water_width)
            if lh >= rh: # That means the right is shorter, there may be a taller bar == more volume if we go left
                right -= 1
            else:
                left += 1
        
        return max_volume
