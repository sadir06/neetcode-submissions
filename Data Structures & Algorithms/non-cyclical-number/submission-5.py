class Solution:
    def isHappy(self, n: int) -> bool:
        string = str(n)
        previous = set() # This is the genius part - we add each new string to the set and if we find any duplicates, we return False!
        previous.add(int(string))
        sum = 0
        counter = 0
        while string != "1":
            for char in string:
                sum += (int(char) ** 2)
            if sum in previous:
                return False
            string = str(sum)
            previous.add(sum)
            sum = 0
        return True

            