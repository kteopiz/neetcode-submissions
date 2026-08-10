# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = n1 = n2 = None

        if not list1:
            return list2
        if not list2:
            return list1
        if not list1 and not list2:
            return None


        if list1.val <= list2.val:
            start = list1
            n1 = list1.next
            n2 = list2
        else:
            start = list2
            n1 = list1
            n2 = list2.next
        runner = start

        while n1 and n2:
            if n1.val <= n2.val:
                runner.next = n1
                n1 = n1.next
                runner = runner.next
            else:
                runner.next = n2
                n2 = n2.next
                runner = runner.next
        
        runner.next = n1 or n2
        
        return start
            
        # cover one empty one not case

