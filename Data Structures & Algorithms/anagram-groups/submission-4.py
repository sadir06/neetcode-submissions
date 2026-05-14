class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: # Next instead of sorting every string, represent every string by the frequency of its characters, 2 strings are only identical if their frequencies are the same
        res = defaultdict(list) # each key is a 26 length tuple representing character frequencies
        for s in strs: # For each string
            count = [0] * 26
            for c in s: # For each char in each string
                count[ord(c) - ord('a')] += 1 # Go to the structured index (start at index 0 so subtract ord a) and increment whichever letter we have
                # Next we will turn this into a tuple and use it as a key in res
            res[tuple(count)].append(s) # Append the relevant string at the specific count, and we will return a list of lists in any order
        
        return list(res.values()) # returns a list of lists where the inner lists are the grouped anagrams with the same frequencies as their "count" list is the same
