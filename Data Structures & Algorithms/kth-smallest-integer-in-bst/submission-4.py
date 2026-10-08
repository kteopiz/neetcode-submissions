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
            # self.res check to cut ops early
            if root is None or self.res is not None:
                return 0
            
            dfs(root.left)

            # self.res check to cut ops early
            if self.res is not None:
                return

            # count this node as one of k-th
            self.k -= 1

            # similar to self.res check if k == 0 res is already found so to cut ops early
            if self.k == 0:
                self.res = root.val
                return
            
            dfs(root.right)
        
        dfs(root)
        return self.res


            

            
            



