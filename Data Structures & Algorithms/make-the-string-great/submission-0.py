class Solution:
    def makeGood(self, s: str) -> str:
        """
        We are given a string, and we ahve to repeatedly remove an adjacent pair when the characters are the same english letters in opposite cases, sch as a, A, or B, b. Continue until no such pair remains and return the resulting string. What we can do is put these onto a stack, and check if the incoming one is the upper case or lower case of what is on the stack. Basically we can turn it upper if the stack top is upper or lower, and do a comparison to see if they are the same string, nad if they are, we pop the stack, else we add to the stack. Then, we make sure to never hit a colision. At the end we return what is on the stack. This way we will never add anything that casues a collision. Looking at abBA, we will add, a, then b, and then B will make us POP b, and then A, will make us pop a, and then we will return "".join(stack), simple. 
        """
        stack = []

        for char in s:
            if not stack or (stack[-1].isupper() and char.isupper()) or (stack[-1].islower() and char.islower()):
                stack.append(char)
            elif (char.isupper() and stack[-1].islower()) or (char.islower() and stack[-1].isupper()):
                new_char = char.lower()
                other_char = stack[-1].lower()

                if new_char == other_char:
                    stack.pop()
                else:
                    stack.append(char)
        return "".join(stack)