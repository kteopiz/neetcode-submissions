class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h cannot be < len(piles), else the problem is impossible
        # if h == len(piles), the only solution is k = max(piles)
        # k > 0 must be true as well since the min of each pile is 1

        l, r = 1, max(piles)
        res = float('inf')
        while l <= r:
            m = (l + r) // 2

            currH = 0
            for p in piles:
                currH += math.ceil(p / m)

            # if we took too much time, we need MORE eating capacity
            # also an invalid k value
            if currH > h:
                l = m + 1
            else:
                res = min(res, m)
                r = m - 1
        return res

                
        