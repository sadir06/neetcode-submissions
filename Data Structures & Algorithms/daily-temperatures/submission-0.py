class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        
        for i, temp in enumerate(temperatures):
            curr_days = 1
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temp:
                    stack.append(curr_days)
                    break

                else:
                    curr_days += 1

                if j == len(temperatures) - 1:
                    stack.append(0)

        if len(stack) != len(temperatures):
            stack.append(0)
            



        return stack