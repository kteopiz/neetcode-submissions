# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        t = head
        p = None

        # Add prev pointers and move t to the tail
        while t.next:
            t.prev = p
            p = t
            t = t.next

        t.prev = p

        h = head

        while h is not t and h.next is not t:
            next_h = h.next   # Save next left node
            prev_t = t.prev   # Save next right node

            h.next = t        # Left -> right
            t.next = next_h   # Right -> next left

            h = next_h
            t = prev_t

        # Finish the middle
        if h is t:
            # Odd number of nodes: both pointers reached the same node
            h.next = None
        else:
            # Even number of nodes: h and t are adjacent
            h.next = t
            t.next = None