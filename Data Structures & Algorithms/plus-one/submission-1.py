class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      
        # 1. Turn the list of integers into a list of strings
        # 2. Join the list of strings into a single string
        num_str = "".join(map(str, digits))
        
        # 3. Convert that string into an integer and add 1
        incremented_num = int(num_str) + 1
        
        # 4. Turn it back into a string
        new_str = str(incremented_num)
        
        # 5. Iterate through the string and turn each character back into an integer
        return [int(char) for char in new_str]
            