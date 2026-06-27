class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        stack = []

        for char in s:
            if char not in brackets:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    output = stack.pop()
                    if output != brackets[char]:
                        return False

        return not stack # A real stack should be empty at the end
        
