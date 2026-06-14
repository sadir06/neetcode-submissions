class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: # Next instead of sorting every string, represent every string by the frequency of its characters, 2 strings are only identical if their frequencies are the same
        res = defaultdict(list)

        for string in strs:
            strings = [0] * 26
            for char in string:
                strings[ord(char) - ord('a')] += 1
            res[tuple(strings)].append(string) # Turn it into a tuple as lists are lowkey immutable
        return list(res.values()) # Return the values as a list