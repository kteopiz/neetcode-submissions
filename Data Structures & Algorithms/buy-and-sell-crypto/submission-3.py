class Solution:
    def maxProfit(self, p: List[int]) -> int:
        l = 0
        res = 0

        for r in range(len(p)):
            if p[r] < p[l]:
                l = r
            res = max(res, p[r] - p[l])
        return res



                