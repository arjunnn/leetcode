from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amounts = [amount + 1] * (amount + 1)
        amounts[0] = 0
        for j in range(1, amount + 1):
            for coin in coins:
                if j - coin >= 0:
                    amounts[j] = min(amounts[j], 1 + amounts[j-coin])
        return amounts[-1] if (amounts[-1] != amount + 1) else -1
