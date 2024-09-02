class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        buy= prices[0]
        
        for i in range(1,n):
            profit= max(profit,prices[i]- buy)
            buy = min(buy, prices[i])
                
                 
                
        return profit
        