# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverseList(head):
            p = None
            runner = head
            while runner:
                t = runner.next
                runner.next = p
                p = runner

                if t:
                    runner = t
                else:
                    break
            test = runner
            while test:
                print(test.val)
                test = test.next
            
            return runner
        
        runner = head
        while runner:
            runner.next = reverseList(runner.next)
            runner = runner.next

