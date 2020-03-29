class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # initialize dp array
        numCoins = [math.inf]*(amount + 1)
        # base case, it takes 0 coins to make the sum 0
        numCoins[0] = 0
        
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    # get the minimum number of ways to make up amount-coin in coins
                    # and add 1 for the additional coin
                    numCoins[i] = min(numCoins[i], numCoins[i-coin]+1)
                    
        # if there's no way to create the sum given the denominations in the coins list
        if numCoins[-1] == math.inf:
            return -1
        return numCoins[-1]