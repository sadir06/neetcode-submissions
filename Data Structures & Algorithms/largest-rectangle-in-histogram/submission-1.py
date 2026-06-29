class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # This is a monotonic stack of indices
        max_area = 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                out = stack.pop() # Index of the bar whose rectangle we're finalising right now
                left = stack[-1] if stack else -1
                current_area = heights[out] * (i - left - 1)
                max_area = max(max_area, current_area)
            stack.append(i)


        n = len(heights)
        while stack:
            out = stack.pop()
            left = stack[-1] if stack else -1
            current_area = heights[out] * (n - left - 1)
            max_area = max(max_area, current_area)

        return max_area