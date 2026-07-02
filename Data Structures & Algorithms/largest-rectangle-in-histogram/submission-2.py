class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # We can use a monotonic stack in this quesiton
        # A monotonic stack is one that checks whether a new value is greater than the top of the stack and it keeps popping the top
        # This is useful here, because when we pop values, we can calculate their volume, and use that to calculate our volume for what that square could have been -> Because when we pop those values, that means they are the maxmium rectangle being formed -> Just be careful calculating the range here, as it can vary 
        stack = []
        max_volume = 0 
        for i, h in enumerate(heights): # For each height, we need to find the maximum rectangle, and we will return the maximum area this way
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop() # We store these to calculate the value
                max_volume = max(max_volume, height * (i - idx))
                start = idx 
            stack.append((start, h))

        for i, h in stack:
            max_volume = max(max_volume, h * (len(heights) - i))

        return max_volume