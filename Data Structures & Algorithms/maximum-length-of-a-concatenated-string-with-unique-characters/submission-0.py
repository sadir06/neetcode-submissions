class Solution:
    def maxLength(self, arr: list[str]) -> int:
        """
        We have an array of strings arr. A string s if formed by the concatentation of a subsequence of arr that has unique characters. Return the max possible lelngth of s. A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the elements. Looking at the first example we see the answer is 4, beacuse there are 5 valid ones (we can only concatenate 2 strings), and out of all of them, we can clearly see that the final 2 are of length 4, and have no overlapping letters. They have all unique letters. Hmmm, so we need to think about this carefully. 
        """
        max_len = float("-inf")
        visiting = set()
        def dfs(i):
            nonlocal max_len
            if i == len(arr):
                max_len = max(max_len, len(visiting))
                return
            found = False
            for char in arr[i]:
                if char in visiting:
                    found = True
                    break
            if len(set(arr[i])) != len(arr[i]):
                found = True
            if not found:
                for char in arr[i]:
                    visiting.add(char)
                dfs(i + 1)
                for char in arr[i]:
                    visiting.remove(char)
                dfs(i + 1)
            else:
                dfs(i + 1)
            return     
        dfs(0)
        return max_len