class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
            visited = set()
            treeMap = {i: [] for i in range(n)}
            for root, node in edges:
                treeMap[root].append(node)
                treeMap[node].append(root) # An undirected graph goes both ways

            def dfs(node, parent):
                if node in visited:
                    return False # We have hit a cycle
                visited.add(node)
                for neighbor in treeMap[node]:
                    if neighbor == parent:
                        continue # Just looking backward, ignore it                    
                    
                    if not dfs(neighbor, node):
                        return False
                return True


            return dfs(0, -1) and len(visited) == n
