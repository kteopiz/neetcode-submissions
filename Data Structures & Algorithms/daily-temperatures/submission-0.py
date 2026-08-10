class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0] * len(temps)
        stack = []

        for i, t in enumerate(temps):
            if not stack:
                stack.append((t, i))
            else:
                while stack and stack[-1][0] < t:
                    top = stack[-1]
                    topTemp = top[0]
                    topIndex = top[1]
                    res[topIndex] = i - topIndex
                    stack.pop()
                stack.append((t,i))
        return res