# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Preorder: Root -> Left -> Right
        # Inorder:  Left -> Root -> Right
        #
        # Key idea:
        # Preorder tells us which node is the root.
        # Inorder tells us which nodes belong to its left/right subtrees.

        # Map each value to its index in inorder for O(1) lookup
        in_order_hm = {val: idx for idx, val in enumerate(inorder)}

        # Global variable to track the next root in preorder (shared across recursive calls)
        pre_order_idx = [0]

        def arr_to_tree(l, r):
            # No nodes remaining in this inorder range
            if l > r:
                return None

            # Next preorder value is the root of the current subtree
            root_val = preorder[pre_order_idx[0]]
            pre_order_idx[0] += 1
            root = TreeNode(root_val)

            # Root's inorder index divides left and right subtrees
            mid = in_order_hm[root_val]

            # Build left subtree first (preorder visits left before right)
            root.left = arr_to_tree(l, mid - 1)

            # Build right subtree using remaining inorder range
            root.right = arr_to_tree(mid + 1, r)

            return root

        # Start with the entire inorder array
        return arr_to_tree(0, len(inorder) - 1)

        # Time: O(n) - Each node processed once, O(1) hashmap lookup
        # Space: O(n) - Hashmap + recursion stack