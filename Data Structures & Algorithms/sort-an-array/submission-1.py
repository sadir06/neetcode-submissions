class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, M, R): # array, left, mid, right
            left, right = arr[L:M + 1], arr[M + 1:R + 1]
            i, j, k = L, 0, 0
            
            while j < len(left) and k < len(right): # When recombining pick the smaller value in each list at each index and add it to arr
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            while j < len(left): # Add anything remaining from left, and right
                arr[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1

        def mergeSort(arr, l, r): # Given an array, left and right, perform merge sort on it
            if l >= r:
                return 
            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)

        mergeSort(nums, 0, len(nums) - 1)
        return nums