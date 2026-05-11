class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st = sorted(s)
        tt = sorted(t)
        return st==tt