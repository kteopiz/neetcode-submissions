# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # cant i build bottom up the path?
        # if add all Nones for the sake of structure

        def dfs(root):
            if root is None:
                return [None]
            
            left = dfs(root.left)
            right = dfs(root.right)

            return [root.val] + left + right

        return dfs(p) == dfs(q)

             


    
            
