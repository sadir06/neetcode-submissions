class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        """
        Given a triangle array, return the min path sum from top to bottom. So at each level, we pick the smallest each time. And then we return the sum. Simple?
        """
        dp = triangle[-1] # len(trinagle) = 1 atleast
        for i in range(len(triangle) - 2, -1, -1):
            temp = triangle[i] 
            left, right = 0, 1
            while right < len(dp):
                temp[left] += min(dp[left], dp[right]) 
                left += 1
                right += 1
            dp = temp[:]
        return dp[0]