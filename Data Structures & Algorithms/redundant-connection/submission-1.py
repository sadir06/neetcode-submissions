class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        treeMap = {i: [] for i in range(1, n + 1)}

        def dfs(source, target, visited):
            if source == target:
                return True # We have found the target

            visited.add(source)

            for neighbor in treeMap[source]:
                if neighbor not in visited:
                    if dfs(neighbor, target, visited):
                        return True
            return False # We we ever reach the end without hitting te target, we return False

        for u, v in edges:
            visited = set()
            if dfs(u, v, visited): # We run this to see if we can somehow find a cycle between v and u, if u can somehow path to v without going backwards, that means we have a cycle
                return [u, v]
            else:
                treeMap[u].append(v) # This node is safe, so we can go through it. 
                treeMap[v].append(u)
    