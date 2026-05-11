class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {} # Use hash maps, because the letters in t could be out of order in the substring, this is an easy way to count occurrences + duplicates
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have = 0
        need = len(countT)
        res = [-1, -1]
        resLen = float("inf")
        l = 0

        for r in range(len(s)):
            char = s[r] # Easy to identify the current char
            window[char] = 1 + window.get(char, 0) # if the char exsists in s & t, add 1 to it
            if char in countT and window[char] == countT[char]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r] # This window of terms is equal to the result

                window[s[l]] -= 1 # Make the window smaller
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res # Split res, and assign them to l, and r at the very end of the loop
        return s[l : r + 1] if resLen != float("inf") else ""
        
