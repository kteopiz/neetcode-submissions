class Solution:
    def maxProfit(self, p: List[int]) -> int:
        l, r = 0, len(p) - 1
        res = 0
        m = p[0]

        for i in p:
            m = min(m, i)
            res = max(res, i - m)
        
        return res

                