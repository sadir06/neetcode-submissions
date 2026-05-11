class Solution:
    def isPalindrome(self, s: str) -> bool:
        s3 = []
        
        for char in s:
            if char.isalnum():
                s3.append(char.lower())
        
        s4 = "".join(s3)

        return s4[::-1] == s4