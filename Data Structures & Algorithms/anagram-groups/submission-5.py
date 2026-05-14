class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: # Next instead of sorting every string, represent every string by the frequency of its characters, 2 strings are only identical if their frequencies are the same
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(s)

        return list(res.values())
                