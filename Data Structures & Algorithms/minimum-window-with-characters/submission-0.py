from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        min_len = float("inf")
        t_count = Counter(t)

        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i : j + 1]

                if self.is_valid(substring, t_count):
                    if len(substring) < min_len:
                        min_len = len(substring)
                        res = substring

        return res

    def is_valid(self, substring, t_count):
        sub_count = Counter(substring)
        for char in t_count:
            if sub_count[char] < t_count[char]:
                return False
        return True