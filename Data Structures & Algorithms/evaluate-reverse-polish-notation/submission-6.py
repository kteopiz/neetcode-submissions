class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        
        ops = {
            '+' : lambda x, y: x + y,
            '-' : lambda x, y: x - y,
            '*' : lambda x, y: x * y,
            '/' : lambda x, y: x / y
        }

        stack = []
        for t in tokens:
            if t in ops:
                # always want deeper num to be the res (n2)
                y = int(stack.pop())
                x = int(stack.pop())
                temp = ops[t](x, y)
                stack.append(temp)
            else:
                stack.append(int(t))
            print(stack)
        return int(stack[-1])

                



