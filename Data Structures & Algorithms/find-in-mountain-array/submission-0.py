class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # An array is only a mountain array if and only if it is long erthan 3, there is some index i where it is larger in value than all hte vlaues before it, and all vaues after it are also smaller. Makes sense.
        length = mountainArr.length()
        l, r = 1, length - 2
        # Find the peak first
        while l <= r:
            m = (l + r) // 2
            left, mid, right = mountainArr.get(m - 1), mountainArr.get(m), mountainArr.get(m + 1)
            if left < mid < right: # Increasing side we need to keep going to the right
                l = m + 1
            elif left > mid > right: # Decreasing side we need to go to the left
                r = m - 1
            else: # In any other scenario we have found the tip
                break # The current values are at the top
        peak = m # We will always end up shifting until the point where left or right are the tip, nad then that means that we only detect a change once they go one past and become smaller, therefore the middle being the peak

        # Search the left portion
        l, r = 0, peak - 1
        while l <= r:
            m = l + (r - l) // 2
            val = mountainArr.get(m)
            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return m
        
        # Search hte right
        l, r = peak, length - 1
        while l <= r:
            m = l + (r - l) // 2
            val = mountainArr.get(m)
            if val > target:
                l = m + 1
            elif val < target:
                r = m - 1
            else:
                return m
        return -1