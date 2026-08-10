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
                test = test.next
            
            return runner
        
        s = head
        c = 0
        while s:
            c += 1
            s = s.next
        rHalf = None
        sli = c // 2 + 1
        lHalf = head
        s = head

        # include first elem
        count = 1
        while count <= sli:
            if count == sli:
                rHalf = s.next
                s.next = None
            count += 1
            s = s.next
        
        left = lHalf.next
        right = reverseList(rHalf)
        runner = head
        takeLeft = False 
        while left and right:
            if takeLeft:
                runner.next = left
                left = left.next
            else:
                runner.next = right
                right = right.next
            runner = runner.next
            takeLeft = not takeLeft
        runner.next = left or right
