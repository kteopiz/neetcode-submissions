class Solution:
    def trap(self, h: List[int]) -> int:   
        l, r = 0, len(h) - 1

        # bottlenecks based on ur left and right edges of the divot
        # whichever is the shortest determines how much water u can really trap
        # so long as u know the highest border to ur left / right, you know how much 
        # water you can trap
            # ex. if the highest to ur left is 0, there is no way ur trapping any water
            # just like on the 1st and last pos
        
        # running maxiumums 
        maxLeft, maxRight = h[l], h[r]
        res = 0

        while l < r:
            # must update the worst bottle neck
            # think of best time to buy stock, what constrainted profit
            # in this case what constraints trapped water is ur "worse" pointer
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, h[l])
                res += maxLeft - h[l]
            else:
                r -= 1
                maxRight = max(maxRight, h[r])
                res += maxRight - h[r]
        return res
    
