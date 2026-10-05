# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, root, depth):
        if root is None:
            return depth
        ld, rd = 0,0
        
        if root.left:
            ld = self.dfs(root.left, depth)
        if root.right:
            rd = self.dfs(root.right, depth)

        return max(ld, rd) + 1
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0

        if root:
            depth = self.dfs(root, depth)
        
        return depth
        