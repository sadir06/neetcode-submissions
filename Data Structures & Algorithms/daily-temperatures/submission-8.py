class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = [] # This is a stack where we keep a list of days (which are indices) that are waiting to find a warmer day

        for current_day in range(len(results)):
            while stack and temperatures[current_day] > temperatures[stack[-1]]: # we have found the day's problem
                popped_item = stack.pop()
                results[popped_item] = current_day - popped_item # Remember that the stack holds indices so we can use this
            else: # The current day is not warmer, add it to the stack and let it wait it's turn
                stack.append(current_day)

        return results