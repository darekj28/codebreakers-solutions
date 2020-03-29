class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp array to keep track of subproblems
        numWays = [0]*(amount+1)
        # base case, number of ways to create the amount 0 is 1, the empty set
        numWays[0] = 1
        
        for coin in coins:
            for i in range(coin, amount+1):
                # the number of ways to make the amount i is the sum of the way to make i-coin for each coin in coins
                numWays[i] += numWays[i-coin]
        return numWays[-1]