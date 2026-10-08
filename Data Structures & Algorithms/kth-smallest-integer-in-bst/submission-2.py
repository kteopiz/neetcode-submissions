# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.bucket = [0] * 10001

        def dfs(root):
            if root is None:
                return None

            self.bucket[root.val] += 1

            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        for i in range(len(self.bucket)):
            k -= self.bucket[i]
            if k == 0:
                return i