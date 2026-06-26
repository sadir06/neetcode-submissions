class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count, window = {}, {}
        left, right = 0, 0
        res, min_len =  [-1, -1], float("inf")

        for char in t:
            count[char] = 1 + count.get(char, 0)
        need, have = len(count), 0

        while right < len(s):
            window[s[right]] = 1 + window.get(s[right], 0)
            if (s[right] in count) and (window[s[right]] == count[s[right]]): # Second can obviously only be true if the first part is true
                have += 1 # We have this counter, we are good

            while have == need: # We have a valid window, we can cut off the rest of it on the left side
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    res = [left, right]
                current_len = right - left + 1
                left_char = s[left]
                window[left_char] -= 1
                if left_char in count and window[left_char] < count[left_char]:
                    have -= 1
                left += 1
            right += 1

        return s[res[0] : res[1] + 1] if min_len != float("inf") else ""
