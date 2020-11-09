from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0: profit += tmp
        return profit

if __name__ == '__main__':
    prices = [3,9,20,15,7]
    way = Solution()
    result=way.maxProfit(prices)
    print(result)