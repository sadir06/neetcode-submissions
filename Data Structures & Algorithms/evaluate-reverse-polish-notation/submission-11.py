class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(["+", "-", "*", "/"]) # Allows for easy O(1) search

        for curr in tokens:
            if curr not in operators:
                # This means that we are on a number
                stack.append(int(curr)) # Turn it into an integer
            else:
                a, b  = stack.pop(), stack.pop() # Stack cannot be empty here as per the rules we will always have altleast a stack size of 2, actually always exactly a stack size of 2
                if curr == "+":
                    # We add the terms in the stack
                    stack.append(a + b)
                elif curr == "-":
                    stack.append(b - a)
                elif curr == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(b / a))
            
        return stack[-1]