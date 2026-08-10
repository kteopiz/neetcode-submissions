class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # from the left we always keep the LOWEST boundary we find
            # if this is lower than top, keep popping higher parts
            # if this is greater add it to the top
        # we keep track of how many pops we could track, this represents the number of rectangles
        # to the left of the current height that are GREATER than it, which can be used by any
        # elements ahead of it of the same or lesser value
        res = 0
        leftBounds = [0] * len(heights)
        rightBounds = [0] * len(heights)
        # [h, pops]
        stack = []
        for i in range(len(heights)):
            h = heights[i]
            pops = 0 
            while stack and h <= stack[-1][0]:
                curr = stack.pop()
                pops += curr[1] + 1 
            leftBounds[i] = pops
            stack.append([h, pops])
        
        stack = []
        for i in range(len(heights)-1,-1,-1):
            h = heights[i]
            pops = 0 
            while stack and h <= stack[-1][0]:
                curr = stack.pop()
                pops += curr[1] + 1 
            rightBounds[i] = pops
            stack.append([h, pops])

        print(leftBounds)
        print(rightBounds)

        for i in range(len(heights)):
            best = heights[i] * (leftBounds[i] + rightBounds[i] + 1)
            res = max(best, res)
        return res

        