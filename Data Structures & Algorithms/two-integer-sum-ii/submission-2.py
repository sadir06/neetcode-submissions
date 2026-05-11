class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            addition = target - num
            for l, j in enumerate(numbers):
                if l == i:
                    continue
                elif j == addition:
                    if l > i:
                        return [i + 1, l + 1]
                    elif l < i:
                        return [l + 1, i + 1]
        return []