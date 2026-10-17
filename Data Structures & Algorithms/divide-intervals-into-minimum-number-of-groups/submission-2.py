class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        """
        So we have a set of normal intervals, and we have to place every inclusive interval left, right from intervals into exactly one group. Intervals within a group must share no point. Touching at an endpoints countrs as an intersection and they must be put into separate groups. An interval may just have a single point, nad duplicate intervals are separate entries that must each have their own group. REturn the smallest number of possible groups. OK, so we just need to pick a count of unique groups to place these intervals into, it's not necessary that we have to keep the groups themselves, though, I think it can be helpful to store the current inclusive overall range for the current group. This will help us determine if the current interval can go into one of the groups,a nd if not, we create a new group, with the current range of the interval, and that range increases whenever we add in a new, non overlapping point. We can also start off by sorting, and since this might have a greedy solution, as we want to give individual groups to the ones that overlap with the most things, we can start off by sorting in reverse (largest to smallest) with respect to the 2nd term as those will gives us the largest ending ranges. THis will help us determine overlapping ranges right next to us. Let's try it. Trying it on the small first example, we sort it as 3, 5, , 1, 3, and then we start comparing every interval to the one on it's next, looking at 3, 5, and then seeing that it does overlap with 1/3, so we know that we need a new group for 3-5, then we go to 1-3, check if it fits into any current groups and because it doesn't we put it in a new group and return len(groups). IN the 3rd example, we add in 7-7, then 4-5 goes int he same group, and so does 1-2, beacuse the ranges don't overlap. The final range would be 1-7, but nothing overlaps, so we just get one group. OK, lets implement this. Honestlly not sure what brute force here would be, but my solution is about O(n * k) where k = approx(len(groups))
        """
        intervals.sort(reverse=True, key=lambda x : (x[1], x[0])) # Sort in reverse with respect to the 2nd term first
        groups = []
        for interval in intervals:
            found = False
            start, end = interval
            if not groups: # There is not a single group and we know that the smallest group size is 1, so we need to atleast have one, and add this into it.
                groups.append([start, end])
                continue # Nothing else to see here
            for group, n_interval in enumerate(groups): # Check every group in the current list, and check if we are able to get into any of them, and if not, we add our own new group
                n_start, n_end = n_interval
                if (start < n_start and end < n_start) or (start > n_end and end > n_end): # The new range literally has to me greater than both so basically both have to be under the start or over the end line
                    groups[group][0] = min(start, n_start)
                    groups[group][1] = max(end, n_end)
                    found = True
                    break 
            if not found: # We didn't find a group to put it into
                groups.append([start, end])
        return len(groups)
