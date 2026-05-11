class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            key = "".join(sorted(string))
            result[key].append(string) #Since we have sorted them, cats == acts. Therefore, it will add to the same location in the hashmap. The primary difference is that it will add the actual string to that location as key is sorted but string contains the original string. We need to take this and use it to group together strings at the same key value. 
        result2 = list(result.values())
        return result2

