class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            char = s[i]
            if char != "]":
                stack.append(char)
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop() # Pop off the "["
            
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)
            
        return "".join(stack)