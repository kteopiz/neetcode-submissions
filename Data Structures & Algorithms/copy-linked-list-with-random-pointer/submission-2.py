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

        return seen[head]
