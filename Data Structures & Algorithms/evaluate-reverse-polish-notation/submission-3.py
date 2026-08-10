class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+', '*', '-', '/'}

        for t in tokens:
            print(stack)
            if t in ops:
                n = 0
                o1 = int(stack.pop())
                o2 = int(stack.pop())
                match t:
                    case '+':
                        n = o1 + o2
                    case '-':
                        n = o2 - o1
                    case '*':
                        n = o1 * o2
                    case _:
                        n = int(o2 / o1)
                stack.append(n)
            else:
                stack.append(int(t))
        return stack[0]