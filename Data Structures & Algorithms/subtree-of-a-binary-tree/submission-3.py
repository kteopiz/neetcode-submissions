# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # root == subRoot 

        # helper that is same as sameTree
        def sameTree(root, subRoot):
            if not root and not subRoot:
                return True
            
            if not root or not subRoot:
                return False
            
            if root.val != subRoot.val:
                return False
            
            return sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right)
        
        # edge: null node always findable in any tree
        # guranteed 1 node by restrictions though
        # if subRoot is None:
        #     return True

        # isSubtree will traverse the tree until a sameTree match occurs
        # if ever root == None we are out of candidates 
        if root is None:
            return False

        if sameTree(root, subRoot):
            return True

        # just because this is not a node that produces same subtree as subRoot, does not mean it DNE in the tree
        # try finding subRoot in the left and right subtrees of root

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

        
        