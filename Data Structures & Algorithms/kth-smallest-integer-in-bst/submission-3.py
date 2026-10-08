# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = None
        self.k = k
        
        def dfs(root):
            if root is None:
                return 0
            
            dfs(root.left)

            if self.k == 1 and self.res is None:
                self.res = root.val
            else:
                self.k -= 1
            
            dfs(root.right)
            


        
        dfs(root)
        return self.res


            

            
            



