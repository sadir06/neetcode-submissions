class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        maxWeight = max(people)
        count = [0] * (maxWeight + 1) # We will use this to cound the frequency of each weight
        res = 0
        for person in people:
            count[person] += 1
        idx, i = 0, 1
        while idx < len(people):
            while count[i] == 0:
                i += 1
                continue
            people[idx] = i
            count[i] -=1
            idx += 1
        l, r = 0, len(people) - 1
        while l <= r:
            remain = limit - people[r] 
            r -= 1
            res += 1
            if l <= r and people[l] <= remain:
                l += 1
        return res
