"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        res = Node(-1)
        rr = res
        runner = head
        seen = {}

        # deal w/ empty list pre computations
        if not head:
            return None

        while runner:
            # val, next hash, random hash
            seen[runner] = Node(runner.val, None, None)
            runner = runner.next
        
        runner = head
        while runner:
            curr = seen[runner]
            curr.next = seen[runner.next] if runner.next else None
            curr.random = seen[runner.random] if runner.random else None
            runner = runner.next
        
        # test = seen[head]
        # while test:
        #     print(test.val, test.next or None, test.random or None)
        #     test = test.next

        
        # runner = head
        # # for k, v in seen.items():
        # #     print(k, v)
        # while runner:
        #     rr.val = seen[runner][0]
        #     rr.next = Node(-1) if runner.next else None # dummy

        #     originalRand = runner.random
        #     print(seen.get(originalRand, None))
        #     rr.random = Node(seen[originalRand][0], seen[originalRand][1], seen[originalRand][2]) if originalRand else None

        #     # rr.next = Node(seen[runner.next][0], seen[runner.next][1], seen[runner.next][2]) if runner.next else None
        #     # print(rr.val, seen.get(runner.random, None))
        #     # rr.random = Node(seen[runner.random][0], seen[runner.random][1], seen[runner.random][2]) if runner.random else None
        #     rr = rr.next
        #     runner = runner.next

        return seen[head]
