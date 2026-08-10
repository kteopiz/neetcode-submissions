class Solution:
    def isValid(self, s: str) -> bool:
        ht = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        stack = []


        for b in s:
            if b not in ht:
                stack.append(b)
            else:
                if not stack or stack[-1] != ht[b]:
                    return False
                else:
                    stack.pop()
            print(stack)
            
        return not stack
