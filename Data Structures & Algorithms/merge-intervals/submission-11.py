class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0]) # Sort first so lookaheads actually work!
        output = []

        for i, interval in enumerate(intervals):
            if not output or output[-1][1] < interval[0]:
                output.append(interval) # Safe to append, there's no overlap
            else:
                # We have an overlap, merge it with the last item in the output
                prev = output.pop()
                output.append([min(prev[0], interval[0]), max(interval[1], prev[1])])

        return output
        