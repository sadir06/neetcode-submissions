class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 2 pointers method - take 2 pointers starting at the left
        # and the right. Check if the letters that they see are equal. If they are, increment them
        l, r = 0, len(s) - 1

        while l < r: # Loop until l and r are equal 
            while l < r and not s[l].isalnum(): # Only letters allowed
                l += 1
            while l < r and not s[r].isalnum(): #Skip punctuation, but still increment
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1 #Increment
            r -= 1

        return True # If you reach the end successfully



        

