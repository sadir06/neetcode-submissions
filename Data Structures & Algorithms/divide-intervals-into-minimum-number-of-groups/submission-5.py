class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        """
        So we have a set of normal intervals, and we have to place every inclusive interval left, right from intervals into exactly one group. Intervals within a group must share no point. Touching at an endpoints countrs as an intersection and they must be put into separate groups. An interval may just have a single point, nad duplicate intervals are separate entries that must each have their own group. REturn the smallest number of possible groups. OK, so we just need to pick a count of unique groups to place these intervals into, it's not necessary that we have to keep the groups themselves, though, I think it can be helpful to store the current inclusive overall range for the current group. This will help us determine if the current interval can go into one of the groups,a nd if not, we create a new group, with the current range of the interval, and that range increases whenever we add in a new, non overlapping point. We can also start off by sorting, and since this might have a greedy solution, as we want to give individual groups to the ones that overlap with the most things, we can start off by sorting in reverse (largest to smallest) with respect to the 2nd term as those will gives us the largest ending ranges. THis will help us determine overlapping ranges right next to us. Let's try it. Trying it on the small first example, we sort it as 3, 5, , 1, 3, and then we start comparing every interval to the one on it's next, looking at 3, 5, and then seeing that it does overlap with 1/3, so we know that we need a new group for 3-5, then we go to 1-3, check if it fits into any current groups and because it doesn't we put it in a new group and return len(groups). IN the 3rd example, we add in 7-7, then 4-5 goes int he same group, and so does 1-2, beacuse the ranges don't overlap. The final range would be 1-7, but nothing overlaps, so we just get one group. OK, lets implement this. Honestlly not sure what brute force here would be, but my solution is about O(n * k) where k = approx(len(groups))
        """
        bucket = [0] * (10**6 + 2)
        best = float("-inf")
        for start, end in intervals:
            bucket[start] += 1
            bucket[end + 1] -= 1
        running_num = 0
        for num in bucket:
            running_num += num
            best = max(running_num, best)
        return best




