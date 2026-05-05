class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0

        buy_idx = 0
        sell_idx = 0
        temp_buy_idx = 0

        for i in range(len(prices)):
        # Update minimum price and its index
            if prices[i] < min_price:
                min_price = prices[i]
                temp_buy_idx = i
        
            # Calculate potential profit
            current_profit = prices[i] - min_price
        
            # Update max profit and actual buy/sell indices
            if current_profit > max_profit:
                max_profit = current_profit
                buy_idx = temp_buy_idx
                sell_idx = i
            
        return max_profit