class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        maxLen = 0
        current_length = 0
        left, right = 0, 0

        while right < len(s):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
                current_length -= 1
            else:
                charSet.add(s[right])
                current_length += 1
            right += 1
            maxLen = max(maxLen, current_length)

        return maxLen