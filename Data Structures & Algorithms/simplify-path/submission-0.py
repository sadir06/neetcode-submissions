class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = [] 

        for token in path.split("/"): #Splits into continuous strings like "neetcode" or ".."
            if token == "" or token == ".":
                continue
            elif token == "..":
                if stack:
                    stack.pop() # We are going to pop the entire word string this time, so 1 word is popped
            else: # This is just string
                stack.append(token)

        
        return "/" + "/".join(stack)