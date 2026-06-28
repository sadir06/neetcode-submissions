class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)

        for i in range(len(results)):
            temp_days = 0 # Set this to 0 at the start of each index
            j = i + 1 # You HAVE to start from the next day onwards
            while j < len(temperatures):
                # Once we enter this loop, we increment temp days, because that means there's a day next and we aren't at the last index
                temp_days += 1
                if temperatures[j] > temperatures[i]:
                    results[i] = temp_days # Because we have found a higher temperature on a future day set the index of result to the number of days that this will happen in 
                    break
                j += 1
            
        return results
                

            