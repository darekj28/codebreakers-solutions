class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        # base case
        if len(candidates) == 0:
            return sol
        # back track
        self._backtrack(sol, candidates, target, [], 0, 0)
        return sol
    
    def _backtrack(self, sol, candidates, target, candidateSol, runningSum, i):
        # end the dfs if we pass our target
        if runningSum > target:
            return
        # if we found a valid solution, add it
        if runningSum == target:
            sol.append(candidateSol[:])
            return
        # backtrack through the rest of the array
        for j in range(i, len(candidates)):
            candidateSol.append(candidates[j])
            runningSum += candidates[j]
            self._backtrack(sol, candidates, target, candidateSol, runningSum, j)
            candidateSol.pop()
            runningSum -= candidates[j]