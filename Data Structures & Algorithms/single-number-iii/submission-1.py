class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums, in which exacltly 2 elements appear only once and all the other elements appear exactly twice find hte 2 elements that appear only once. Return it in any order. WRITE AN ALGORITHM THAT RUNS IN LINEAR TIME COMPLEXITY, so we only get onepass throught he array and we have to do constant extra space!!!! What we can do is turn everything into a binary number and we can keep anding those values together. 
        """
        carry = 0 # a XOR with 0 = a
        for num in nums:
            carry = carry ^ num # bitwise XOR
        carry = carry & -carry 
        A, B = 0, 0
        for num in nums:
            if num & carry == 0:
                A = A ^ num
            else:
                B = B ^ num
        return [A, B]

