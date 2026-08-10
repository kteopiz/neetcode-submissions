class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # For each bar, we want to know:
        #   How many consecutive bars on the left are >= me?
        #   How many consecutive bars on the right are >= me?
        #
        # If we know those two widths, then this bar can be the
        # limiting (minimum) height of a rectangle whose width is:
        #
        # left + right + 1
        #
        # Monotonic stacks let us compute these widths in O(n).

        res = 0

        # the key thing question is asking at THIS current bar:
            # how much to my left is >= to me
            # same for the right
        # when we know this question, we know how much we can expand both ways
            # O(n^2) -> go both ways for each bar, if everything is a 1 this goes insane 
        leftBounds = [0] * len(heights)
        rightBounds = [0] * len(heights)

        # How do I know how many to the left of my current bar is >= to it?
            # Use a stack to represent what we have seen so far
            
            # Steps:
                # Resolve everything we have seen that is greater than current
                # Ex. I am at h=1, I can pop everything before me > 1, and can gurantee 
                # Everything before me is greater than me. (1)
                    # If I just save all the pops I did, I essentially save the width ANY
                    # Element ahead that is <= to me can take up
                # If I run into an element greater than the top of the stack keep it
                    # This greater element might meet meet a smaller element 
                    # Ex. 1, 5, when we see 4, it can use BOTH of us
                # TLDR: Resolve everything >= current h
                    # Count pops -> rep. # squares >= this stack elem
                    # Save all elements since greater elements might be usable by other elements
            # This logic is REPEATABLE for the right bounds going the other direction
                

        # [h, pops]
        stack = []
        for i in range(len(heights)):
            h = heights[i]
            pops = 0 
            while stack and h <= stack[-1][0]:
                curr = stack.pop()
                
                # A key element to the solve: 
                # When we pop a bar, we inherit:
                    #   1. the bar itself (+1 width)
                    #   2. all width that bar had already accumulated
                    # This lets us compress many bars into a single count.
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

        for i in range(len(heights)):

            # slight detail: we get how far it can extend both ways AND include its own square for width
            best = heights[i] * (leftBounds[i] + rightBounds[i] + 1)
            res = max(best, res)
        return res

        