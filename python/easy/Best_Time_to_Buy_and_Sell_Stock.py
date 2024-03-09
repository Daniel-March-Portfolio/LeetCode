class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price_idx = 0
        max_price_idx = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[max_price_idx]:
                max_price_idx = i
            elif prices[i] < prices[min_price_idx]:
                max_profit = max(max_profit, prices[max_price_idx] - prices[min_price_idx])
                min_price_idx = i
                max_price_idx = i
        return max(max_profit, prices[max_price_idx] - prices[min_price_idx])