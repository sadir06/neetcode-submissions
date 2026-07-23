class Solution:
    def checkValidString(self, s: str) -> bool:
        stack_brackets = []
        stack_stars = []

        for i, char in enumerate(s):
            if char == "(":
                stack_brackets.append(i)
            if char == "*":
                stack_stars.append(i)
            if char == ")":
                if stack_brackets:
                    stack_brackets.pop()
                elif stack_stars:
                    stack_stars.pop()
                else:
                    return False
        while stack_brackets and stack_stars:
            if stack_stars[-1] > stack_brackets[-1]: # This is exactly why we store indices to make sure that the index of the star comes after the bracket!!!
                stack_stars.pop()
                stack_brackets.pop()
            else: # This star is too early and is basically useless
                stack_stars.pop()
        return not stack_brackets # if we reach the end without any issues, it's all good