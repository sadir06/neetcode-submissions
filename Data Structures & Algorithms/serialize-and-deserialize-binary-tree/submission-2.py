# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.output = []
        def dfs(node):
            # We use this to modify the output list, so we don't return anything
            if not node:
                self.output.append("null")
                return
            self.output.append(str(node.val))
            dfs(node.left)
            dfs(node.right) # left first and then right is the ordering for reconstruction
        dfs(root)
    
        return ",".join(self.output)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data_list = data.split(",")
        self.index = 0 # We need a global pointer to track which iten in the list we are currently looking at
        def build():
            value = data_list[self.index]
            self.index += 1
            if value == "null":
                return
            node = TreeNode(int(value))
            node.left = build()
            node.right = build()
            return node
        return build()