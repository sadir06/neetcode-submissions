class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1]) # key= is the built-in sort method, that takes an optoinal key argument. This expects a function that tells python what value it should look at when sorting items, and by default it sorts it using the very first element. If we want it to look at the second element, we give it x[1] instead. Lambda is just an anonymous, quick inline function that says take one item from thel list and return this specific part of it for python to use as the sorting metric!
        prev_end = intervals[0][1] # We set the end time of the last interval that we decide to keep and initialise it with the smallest end time in the list (because we sorted it, this will naturally be the first one)
        removals = 0 # Just counting how many we decide to remove
        for i, interval in enumerate(intervals):
            if i == 0:
                continue # We have already considered the first interval
            if prev_end > interval[0]: # There is an overlap here, we have a collision
                removals += 1 # Since we sorted by end time, the current interval finishes later and must be thrown away!
            else:
                prev_end = interval[1]
        return removals
