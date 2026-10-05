# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # root == subRoot 

        def dfs(root, subRoot):
            if not root and not subRoot:
                return True
            
            if not root or not subRoot:
                return False
            
            if root.val != subRoot.val:
                return False
            
            return dfs(root.left, subRoot.left) and dfs(root.right, subRoot.right)
        
        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False
        
        if root.val != subRoot.val:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        # found a candidate start of the subRoot
        candidate = dfs(root.left, subRoot.left) and dfs(root.right, subRoot.right)

        if candidate:
            return True

        # invalid candidate look further in the tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

        
        