class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append([val, val])
        else:
            current_min = self.stack[-1][1] # This avoids the problem of popping entirely, because the current min is always the minimum in the last index
            self.stack.append([val, min(val, current_min)])


    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0] # Return the value
        

    def getMin(self) -> int:
        return self.stack[-1][1] # Return the least number so far
        
