class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        # set to keep track of solutions already found
        used = set()
        # sort to allow us to reduce to an n^2 solution for 3sum
        nums.sort()
        for i in range(len(nums)):
            # skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # reduced to 3 sum
            for j in range(i+1, len(nums)):
                # skip duplicates
                if j-1 > i and nums[j-1] == nums[j]:
                    continue
                
                # reduced to sorted two sum
                k = j + 1
                l = len(nums)-1
                while k < l:
                    cand = nums[i] + nums[j] + nums[k] + nums[l]
                    if cand == target and (nums[i], nums[j], nums[k], nums[l]) not in used:
                        used.add((nums[i], nums[j], nums[k], nums[l]))
                        sol.append([nums[i], nums[j], nums[k], nums[l]])
                    elif cand > target:
                        l -= 1
                    else:
                        k += 1
        return sol