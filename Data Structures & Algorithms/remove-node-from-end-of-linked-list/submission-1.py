# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0 
        runner = head

        while runner:
            count += 1
            runner = runner.next

        # when n == count, covers 1 node case automatically
        if count == n:
            return head.next

        skipNext = (count - n)
        count = 1
        runner = head
        while runner:
            if count == skipNext:
                if runner.next:
                    runner.next = runner.next.next
                else:
                    runner.next = None
                break
            count += 1
            runner = runner.next

        return head 
