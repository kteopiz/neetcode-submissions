# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        # if no cycle, slow must hit None
        while slow and fast:
            for i in range(2):
                if fast:
                    fast = fast.next
                else:
                    return False
            if slow and fast:
                if slow is fast:
                    return True
            slow = slow.next
        return False
