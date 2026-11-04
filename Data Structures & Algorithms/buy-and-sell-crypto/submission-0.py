class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            curPrice = prices[i]
            if curPrice > buy:
                res = max(res, (curPrice-buy))
            elif curPrice < buy:
                buy = curPrice

        return res 