class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "/", "*"} # Define as a set for O(1) lookups, a tiny optimisation here because we only do 4 operations at max to do a full search. 

        for i, token in enumerate(tokens):
            if token in operations:
                right = stack.pop()
                left = stack.pop()

                if token == "+":
                    stack.append(right + left)
                elif token == "-":
                    stack.append(left - right)
                elif token == "*":
                    stack.append(right * left)
                elif token == "/":
                    stack.append(int(left/right)) # Forces Python to truncate towards 0

            else: # That means it is an integer string
                stack.append(int(token))

        return stack[0]