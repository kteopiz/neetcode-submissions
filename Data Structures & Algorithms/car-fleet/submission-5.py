class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        stack = []
        sim = []
        
        sim = [[p,s] for p,s in zip(position, speed)]

        sim.sort(key=lambda s: s[0], reverse=True)
        
        # v= d/t

        for p,s in sim:
            t = (target - p) / s
            if not stack:
                stack.append([p,s,t])
            else:
                if t > stack[-1][2]:
                    stack.append([p,s,t])
        print(stack)
        return len(stack)


        
