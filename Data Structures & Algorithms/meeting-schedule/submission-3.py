"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        latest_end_time = 0
        for pair in intervals:
            start_time = pair.start
            end_time = pair.end
            if latest_end_time <= start_time:
                latest_end_time = end_time
            else:
                return False

        return True
