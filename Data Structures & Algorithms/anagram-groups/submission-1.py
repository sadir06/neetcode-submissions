class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            my_counts = [0]*26
            for c in s:
                #This line gives us the ASCII value, setting it as the index (ord('a') is 1, and we subtract the ASCII value of the term by the index)
                my_counts[ord(c) - ord('a')] += 1
            key = tuple(my_counts)
            result[key].append(s)
        return list(result.values())