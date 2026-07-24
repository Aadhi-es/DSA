class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least_price=10000
        profit=0
        for i in range(len(prices)):
            if prices[i]<least_price:
                least_price=prices[i]
            diff=prices[i]-least_price
            if diff>profit:
                profit=diff
        return profit
