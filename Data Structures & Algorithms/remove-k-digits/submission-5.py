class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        This is a monotonic stack question. We are given the decimal string num that represetns a positive integer. We have to delete exactly k digits WITHOUT changing the order of the remaining digits, and return the smallest possible resulting integer as a string. Basically we have to remove the k largest digits. So what can we do here? A greedy solution of removing the largest nums doesn't always work as shown in the example "35241", as removing 3,5 instead of 5, 4, is better. 
        """
        stack = []
        for i in range(len(num)):
            while stack and stack[-1] > num[i] and k > 0:
                stack.pop()
                k -= 1
            stack.append(num[i])
            
        while stack and k > 0:
            stack.pop()
            k -= 1
        num = "".join(stack).lstrip("0")
        if not num:
            return "0"
        return num