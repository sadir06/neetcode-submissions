class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        right, left = 0, 0
        store = {}
        maxLen = 0

        while right < len(s):
            store[s[right]] = store.get(s[right], 0) + 1 # Used to count frequency
            max_freq = max(store, key=store.get) # Use this to get the highest frequency character
            replacements = (right - left + 1) - store[max_freq] # The number of replacements required is the size of the current window + 1 for indexes, and - max frequency bceause we already ahve all the current freuqnecy of the most frequent letter in the window so far, so we don't need to replace those as they are the most common in the window so far, so we replace the other less commom characters. 
            if replacements > k:
                store[s[left]] = store.get(s[left]) - 1 # Reduce the left term
                left += 1
            else:
                maxLen = max(maxLen, right - left + 1)
            right += 1
        return maxLen

