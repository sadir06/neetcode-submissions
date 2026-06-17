class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left <= right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() == s[right].lower():
                    right -= 1
                    left += 1
                    continue
                else:
                    return False
            elif not s[right].isalnum():
                right -=1
                continue
            elif not s[left].isalnum():
                left += 1
                continue
            else:
                print("This cannot happen, and is just a safeguard, if this prints you messed up")
        return True # If we reach this, that means all terms are equal. 
                
        
        

