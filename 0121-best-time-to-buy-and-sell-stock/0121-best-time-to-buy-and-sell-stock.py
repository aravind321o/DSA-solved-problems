class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        buy= prices[0]
        
        for i in prices:
            if i - buy>profit:
                profit = i-buy

            elif buy > i:
                buy = i
                
        return profit
      
     