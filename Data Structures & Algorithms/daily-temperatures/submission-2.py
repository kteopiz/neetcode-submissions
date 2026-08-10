class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            # (temp, idx)
            # is this current candidate able to resolve elements in the stack?
            curr = (temperatures[i], i)
            while stack and stack[-1][0] < curr[0]:
                can = stack.pop()

                # where in res do we update? --> saved index at can[1]
                # what do we update it with --> how many days ahead
                    # since we gurantee elements in the stack are BEFORE our current candidate
                    # just find difference between i and can[i] for the diff in days
                res[can[1]] =  i - can[1]
            stack.append(curr)
        return res
