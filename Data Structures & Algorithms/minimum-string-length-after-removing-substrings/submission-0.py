class Solution:
    def minLength(self, s: str) -> int:
        """
        We are given a string s consisting of only uppercase english letters (26 total). We can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from s (ANY occurence). Return the min possible length of the resulting string you can get. Super simple. Do a one pass check through the string, if you encounter A or C and you are not at the end of the string, check the next letter to see if it is B or D, and if they are, skip the while loop to the next term after, and don't count them. Simple. 
        """
        stack = []
        i = 0
        while i < len(s):
            if s[i] == "B":
                if not stack or stack[-1] != "A":
                    stack.append(s[i])
                else:
                    stack.pop()
            elif s[i] == "D":
                if not stack or stack[-1] != "C":
                    stack.append(s[i])
                else:
                    stack.pop()
            else:
                stack.append(s[i])
            i += 1
        return len(stack)