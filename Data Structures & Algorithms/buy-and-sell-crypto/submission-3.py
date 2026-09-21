class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        candidate = 0

        left, right = 0, 1
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                candidate = max(candidate, prices[right] - prices[left])
            
            right += 1
        
        return candidate