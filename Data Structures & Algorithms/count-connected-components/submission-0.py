class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        num_components = 0
        graphMap = {i : [] for i in range(n)}
        for n1, n2 in edges:
            graphMap[n1].append(n2)
            graphMap[n2].append(n1)
        
        def dfs(i):
            if i in visited:
                return 
            visited.add(i)
            for node in graphMap[i]:
                dfs(node)
            

        for i in range(n):
            if i not in visited:
                num_components += 1
            dfs(i)


        return num_components


        





    