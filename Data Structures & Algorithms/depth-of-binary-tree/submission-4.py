# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, root):
        if root is None:
            return 0
        
        ld = self.dfs(root.left)
        rd = self.dfs(root.right)

        return max(ld, rd) + 1
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # covers edge case of empty tree
        if root is None:
            return 0
        
        # 1 includes the current root + whichever child node has greater depth
        return 1 + max(self.dfs(root.left), self.dfs(root.right))