class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {
            '}':'{',
            ')':'(',
            ']':'['
        }

        for b in s:
            if b not in m:
                stack.append(b)
            else:
                if not stack:
                    return False
                c = stack[-1]
                if m[b] == c:
                    stack.pop()
                else:
                    return False
        return not stack
