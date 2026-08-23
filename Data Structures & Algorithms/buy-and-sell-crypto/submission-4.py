class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2 1 6 7 8
        # 0 -1 4 5 6
        # N 0 5 6 7 

        profit = 0
        buy = prices[0]

        for sell in prices:
            profit = max(profit, sell - buy)
            buy = min(buy, sell)
        return profit
