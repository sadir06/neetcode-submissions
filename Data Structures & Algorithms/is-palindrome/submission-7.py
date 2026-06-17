class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for i in range(len(s) - 1, -1, -1):
            if s[i].isalnum():
                res.append(s[i].lower())
            
        output = "".join(res)
        s_fixed = []
        for i in range(len(s)):
            if s[i].isalnum():
                s_fixed.append(s[i].lower())
        
        s_fixed2 = "".join(s_fixed)
        return output == s_fixed2
        

