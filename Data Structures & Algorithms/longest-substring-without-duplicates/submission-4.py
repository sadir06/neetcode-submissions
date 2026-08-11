class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left, right = 0, 0
        visiting = set()
        visiting.add(s[0])
        max_len, cur_len = 1, 1 # the minimum possible max len is always 1 anyway
        while right < len(s) - 1:
            right += 1 # At each iteration, we increment the right pointer
            while s[right] in visiting: # if we find a duplicate, we must process it, so we kick out all the elements to the left while they are in our set (we don't need to worry about duplicates because we will only ever have 1 instance of a char in our set anyway, and if we encounter a new one when right increments, we remove it and any values that came before it)
                visiting.remove(s[left])
                left += 1
            visiting.add(s[right]) # We then add this char to the set because now it is part of our window
            cur_len = right - left + 1 # this is the count of the values in our window, and not the distance!!!
            max_len = max(max_len, cur_len) # Update this whenever we have a new cur len, it might be the largest.
        return max_len
