"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        starts.sort(), ends.sort()
        s, e, rooms, max_rooms = 0, 0, 0, 0
        while s < len(starts):
            if starts[s] < ends[e]:
                rooms += 1
                s += 1
            else:  # A meeting has finished
                e += 1
                rooms -= 1
            max_rooms = max(max_rooms, rooms)
        return max_rooms