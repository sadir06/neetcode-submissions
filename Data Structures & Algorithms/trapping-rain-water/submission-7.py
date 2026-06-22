class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total_volume = 0
        max_left_list, max_right_list = [0] * n, [0] * n
        for i in range(n - 1):
            if i == 0:
                continue
            max_height = max(max_left_list[i - 1], height[i - 1]) # This is true DP
            max_left_list[i] = max_height
        for i in range(n - 2, -1, -1):
            if i == 0:
                continue
            max_height = max(max_right_list[i + 1], height[i + 1]) # This is true DP
            max_right_list[i] = max_height

        for i in range(n - 1):
            if i == 0:
                continue
            current_height = height[i]
            tallest_wall = min(max_left_list[i], max_right_list[i]) # This means that both walls have atleast the minimum water holding power
            if tallest_wall - current_height <= 0:
                continue
            total_volume += tallest_wall - current_height # Total volume get's added the current indexes water height - current block height. 
        
        return total_volume
        

