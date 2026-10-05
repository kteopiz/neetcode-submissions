# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # best current path = maxDepth of L + maxDepth of R
        # key which node is used as the BRIDGE btwn, not necessarily root node

        # use pythonic self to your advantage for tracking diameter
        self.diameter = 0

        # role of dfs is JUST depth not passing diameter through recursive calls
        def dfs(root):
            if root is None:
                return 0
            
            ld = dfs(root.left)
            rd = dfs(root.right)

            self.diameter = max(
                self.diameter,
                ld + rd # with this node as the bridge btwn left + right subtree is it best diameter?
                )
            
            # keep calculating depth for the parent, responsiblity of the DFS
            return 1 + max(ld, rd)

        dfs(root)

        return self.diameter
        

     
        