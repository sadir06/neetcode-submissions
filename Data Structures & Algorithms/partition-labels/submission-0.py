class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        output = []
        last_occurrence = {char: index for index, char in enumerate(s)}
        max_occurrence = 0
        partition = -1
        for i, char in enumerate(s):
            max_occurrence = max(max_occurrence, last_occurrence[char])

            if i == max_occurrence:
                output.append(max_occurrence - partition)
                partition, max_occurrence = max_occurrence, 0

        
        return output