class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        duplicates = set()
        longest = 0
        while right <= len(s) - 1:
            while s[right] in duplicates:
                duplicates.remove(s[left])
                left += 1
            else:
                duplicates.add(s[right])
            longest = max(longest, (right - left + 1))
        
            right += 1

        return longest