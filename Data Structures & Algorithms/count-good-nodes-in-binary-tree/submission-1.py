# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, m):
            if root is None:
                return 0
            
            isGood = True if root.val >= m else False
            
            m = max(root.val, m)
            if isGood:
                return 1 + dfs(root.left, m) + dfs(root.right, m)
            else:
                return dfs(root.left, m) + dfs(root.right, m)
        
        return dfs(root, root.val)


