# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # best current path = maxDepth of L + maxDepth of R?

        self.diameter = 0

        def dfs(root):
            if root is None:
                return 0
            
            ld,rd=0,0

            if root.left:
                ld = dfs(root.left)
            if root.right:
                rd = dfs(root.right)

            self.diameter = max(
                self.diameter,
                ld + rd # with this node as the bridge btwn left + right subtree is it best diameter?
                )
            
            # keep calculating depth for the parent, responsiblity of the DFS
            return 1 + max(ld, rd)


        dfs(root)

        return self.diameter
        

     
        