class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp)) 
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        left, right, result= 0, len(self.store[key]) - 1, ""
        while left <= right:
            mid = left + (right - left) // 2
            val, time = self.store[key][mid]
            if time == timestamp:
                return val
            elif time <= timestamp:
                result = val
                left = mid + 1 # Aggresively look for a closer time
            else: # This might be allowed we DON'T CUT OUT mid
                right = mid - 1 # Garbage and is greater, just throw it away. 
        return result
        
