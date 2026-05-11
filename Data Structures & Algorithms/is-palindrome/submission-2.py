class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = []
        for ch in s:
            if ch.isalnum(): #.isalnum() - checks if the characther is alphanumeric
                s1.append(ch.lower())
        s1 = ''.join(s1) # Turns a list of charachters into a string

        copy = s1[::-1]

        return copy == s1