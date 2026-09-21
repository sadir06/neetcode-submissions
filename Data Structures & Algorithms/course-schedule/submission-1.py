class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        
        # Initialise all courses with an empty prerequisite list so that we can append prerequisites into it
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(num):
            if num in visited:
                return False
            if preMap[num] == []:
                return True # We have already checked this and verified that it is correct
            output_list = preMap[num] # This gives us an output list
            visited.add(num) # Add this to the list so that we detect 1 number long cycles
            for number in output_list:

                if not dfs(number): # Run bfs on each of the inner graphs
                    return False
            
            # Once a course has finished its DFS and has no cycles, just empty the prerequisite list in the map
            preMap[num] = [] 
            visited.remove(num) # Make sure to remove this at the end
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True