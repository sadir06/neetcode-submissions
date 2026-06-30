class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = nums1, nums2
        if len(n) < len(m): # Always binary search the smaller array
            m, n = n, m

        total = len(m) + len(n)
        half = ((total + 1) // 2)

        left, right = 0, len(m)
        while left <= right: # We binary search to find a valid partition split
            i = left + (right - left) // 2 # Just set this to be the mid value
            j = half - i # This is going to be the partition in the 2nd one because it always has to be half - i, the partitions are mirrored (e.g. half is 6, if i=4, then the 2nd partition in the 2nd array j, must be 6-4=2)

            # Establish the 4 boundaries and use -inf/inf for out-of-bounds
            L1 = m[i - 1] if i > 0 else float("-inf") # Set this to the highest value in the left array (i - 1 because of indexing), as it is sorted
            R1 = m[i] if i < len(m) else float("inf")
            L2 = n[j - 1] if j > 0 else float("-inf")
            R2 = n[j] if j < len(n) else float("inf")

            # Now we check for a valid partition
            if L1 <= R2 and L2 <= R1:
                # FOUND A VALID PARTITION
                if total % 2: # If it is odd, we just return the max number, because an odd total means that there is one sigular merdian
                    return float(max(L1, L2))
                return (max(L1, L2) + min(R1, R2)) / 2 # Else we have 2 median values so we return an average of them!
            # If we don't find a partitoin, we try different values
            elif  L1 > R2:
                right = i - 1 # Too far right in m, move to the left
            else:
                # Too far left in A, move right
                left = i + 1
