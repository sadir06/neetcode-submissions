class Solution:
    def longestPalindrome(self, s: str) -> str:
        result, resLen = "", 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                l, r = i, j
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1

                if l >= r and resLen < (j - i + 1):
                    result = s[i : j + 1]
                    resLen = j - i + 1
        return result