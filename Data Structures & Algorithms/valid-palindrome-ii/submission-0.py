class Solution:
    def isPalindrome(self, string):
        string = string.lower()
        result = list(string)
        output = []
        for num in result:
            if num.isnumeric():
                continue
            output.append(num)
        string2 = "".join(output)
        if string2 == string2[::-1]:
            return True
        else:
            return False
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            string2 = s[:i] + s[i + 1:] # Skip the middle char
            if self.isPalindrome(string2):
                return True
            else:
                continue
        return False