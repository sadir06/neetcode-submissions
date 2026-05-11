class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        hash_map_t, hash_map_s = {}, {} # Define these 2 - Write 2 loops to add all letters, check if equal

        for char in s:
            hash_map_s[char] = 1 + hash_map_s.get(char, 0) # Get's the value of char, if it doesn't exsist, adds 0
        
        for char in t:
            hash_map_t[char] = 1 + hash_map_t.get(char, 0)

        return hash_map_t == hash_map_s