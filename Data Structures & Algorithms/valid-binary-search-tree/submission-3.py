# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, bounds):
            if root is None:
                return True
        
            moreThanMin = bounds[0] is None or root.val > bounds[0]
            lessThanMax =  bounds[1] is None or root.val < bounds[1]

            leftBounds = [
                bounds[0],
                min(root.val, bounds[1]) if bounds[1] else root.val
            ]

            rightBounds = [
                max(root.val, bounds[0]) if bounds[0] else root.val,
                bounds[1]
            ]

            return (
                moreThanMin and
                lessThanMax and
                dfs(root.left, leftBounds) and
                dfs(root.right, rightBounds)
            )
        
        return dfs(root, [None, None])
        