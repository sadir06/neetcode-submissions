class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []
        n, m = len(word1), len(word2)
        if n > m: # n should be the shorter word
            m, n = n, m
        i, j = 0, 0
        left, right = 0, 0

        while right < n:
            if i % 2 == 0:
                output.append(word1[left])
                left += 1
            else:
                output.append(word2[right])
                right += 1
                j += 1 # Increment for the 2nd word here, so that we reach the end of the shortest word regardless
            i += 1
            

        while j < len(word1): # Only one of these 2 while loops can ever be true, because we only reach the end of one word or the other, and since we always look the shortest one, whichever word was longer will always activate
            output.append(word1[j])
            j += 1
        while j < len(word2):
            output.append(word2[j])
            j += 1
        return "".join(output)