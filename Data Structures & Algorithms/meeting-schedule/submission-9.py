"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.end) # Sort by finish times, will make everything easier
        prev_end = intervals[0].end # remember, if we can't attend the first one, we can immediatelyt return false, this is asking is we can attend ALL of our meetings
        for i, interval in enumerate(intervals):
            start, end = interval.start, interval.end
            if i == 0:
                continue 
            if prev_end > start:
                return False
            else:
                prev_end = end
        return True