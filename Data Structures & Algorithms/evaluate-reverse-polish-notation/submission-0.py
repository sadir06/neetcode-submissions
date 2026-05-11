class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens: # Iterates through each item
            if c == "+": # This means that we add the 2 values in the current stack, and pop them
                stack.append(stack.pop() + stack.pop()) # Order doesn't matter for addition

            elif c == "-":  
                a, b = stack.pop(), stack.pop()
                stack.append(b - a) # Order of subtraction matters
            elif c == "*":
                stack.append(stack.pop() * stack.pop()) # Order of multiplication doesn't matter
            elif c == "/":
                a, b = stack.pop(), stack.pop() # Order of division matters
                stack.append(int(float(b) / a)) # float b is for divistion with negative numbers
            else:
                stack.append(int(c)) # Change it into an integer
        
        return stack[0] # Only 1 term should exsist in the output