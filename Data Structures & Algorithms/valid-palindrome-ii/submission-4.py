class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        for i in range(len(s)):
            string2 = s[:i] + s[i + 1:] # Skip the middle char
            if string2 == string2[::-1]:
                return True
        return False