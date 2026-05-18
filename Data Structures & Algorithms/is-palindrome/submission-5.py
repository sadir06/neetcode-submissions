class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''
        for c in s:
            if c.isalnum():
                s2 += c.lower()
        return s2 == s2[::-1]