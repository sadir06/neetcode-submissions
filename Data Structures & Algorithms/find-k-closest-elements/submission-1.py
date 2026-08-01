import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1

        while r - l >= k: # we end it when r and l become the size of k
            if abs(x - arr[l]) <= abs(x - arr[r]): # Remove the element htat it sfarter by moving the poiter inwards
                r -=1
            else:
                l += 1
        return arr[l : r + 1] # arr is already sorted, the closest numbers to x form a contiguous subarray
         #Return the subarray from the 2 points we have found to be working