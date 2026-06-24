class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new_interval = []
        previous_highest_0 = 0
        previous_highest_1 = 0
        intervals.sort()
        for sublist in intervals: # We loop through each sublist, and remember the current range to pass along that information to the next sublist, as we only need to know what the outer bound of the previous sublist was
            if not new_interval:
                previous_highest_0 = sublist[0]
                previous_highest_1 = sublist[1]
                new_interval.append(sublist)
                continue
            
            if previous_highest_1 >= sublist[0]:
                if new_interval:
                    new_interval.pop()
                    previous_highest_1 = max(previous_highest_1, sublist[1])
                    new_interval.append([previous_highest_0, previous_highest_1])
                continue
            
            
            previous_highest_0 = sublist[0]
            previous_highest_1 = sublist[1] # We can always assume that there will only be 2, the start and the end
            new_interval.append([sublist[0], sublist[1]])




        return new_interval
