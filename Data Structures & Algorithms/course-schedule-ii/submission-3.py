class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.output = []
        visited, completed = set(), set()
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(crs):
            if crs in visited:
                return False
            if crs in completed:
                return True # We have already processed this, we don't add it to our thing again
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            self.output.append(crs)
            visited.remove(crs)
            completed.add(crs)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        return self.output