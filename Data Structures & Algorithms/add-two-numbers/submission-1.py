# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        res = ListNode()
        s = res
        c = 0
        while p1 and p2:
            d = p1.val + p2.val + c 
            if d > 9:
                c = 1
                d -= 10
            else:
                c = 0
            s.val, s.next = d, ListNode() if p1.next or p2.next else None
            p1, p2, s = p1.next, p2.next, s.next if s.next else s
        
        r = p1 or p2
        while r:
            d = r.val + c
            if d > 9:
                c = 1
                d -= 10
            else:
                c = 0
            s.val = d
            s.next = ListNode() if r.next else None
            r = r.next
            s = s.next if s.next else s
        
        # if a carry remains add it on
        if c:
            s.next = ListNode(c)

        return res
        
            

