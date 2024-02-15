class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # two pointer
        start_index = 0
        end_index = 1
        max_profit = 0
        
        while end_index < len(prices):
            profit = prices[end_index] - prices[start_index]
            
            if prices[start_index] < prices[end_index]:
                max_profit = max(profit, max_profit)
            else:
                start_index = end_index
            end_index += 1
                
        return max_profit
            
            
            
            
        