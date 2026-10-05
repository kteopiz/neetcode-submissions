# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.balanced = True

        def dfs(root):
            if root is None:
                return 0
            
            ld = dfs(root.left)
            rd = dfs(root.right)

            if abs(ld - rd) > 1:
                self.balanced = False
            
            return 1 + max(ld, rd)
        
        dfs(root)

        return self.balanced

            

        