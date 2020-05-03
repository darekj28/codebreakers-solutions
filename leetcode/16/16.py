class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # sort input array
        nums.sort()
        
        # keep track of closest dist and sum
        closestDist = math.inf
        toReturn = None
        
        # go through triplets
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            j = i + 1
            k = len(nums)-1
            while j < k:
                cand = nums[i] + nums[j] + nums[k]
                if cand == target:
                    return target
                # update closest sum
                if abs(target - cand) < closestDist:
                    closestDist = abs(target-cand)
                    toReturn = cand
                if cand > target:
                    k -= 1
                else:
                    j += 1
        return toReturn