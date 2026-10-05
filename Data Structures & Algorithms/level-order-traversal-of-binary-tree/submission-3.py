# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cur = root
        q = deque()
        res = []
        
        if root is None:
            return res
        # init 
        q.append(cur)
        
        while q:
            cur = q[0]
            nodes = len(q)
            sub = []
            for i in range(nodes):
                top = q.popleft()
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
                sub.append(top.val)
            res.append(sub)
        return res

        
        