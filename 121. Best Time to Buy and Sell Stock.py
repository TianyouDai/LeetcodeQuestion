class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = 0
        largest = 0
        maxPrice = 0
        
        for i in range(len(prices)):
            if prices[i] < prices[smallest]:
                smallest = i
                largest = i
            else:
                if prices[i] > prices[largest]:
                    largest = i
            maxPrice = max(maxPrice, prices[largest] - prices[smallest])
        
        return maxPrice
        
        
        
        
        
        
