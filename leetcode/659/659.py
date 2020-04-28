class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # base case
        if len(nums) < 3:
            return False
        
        numToCount = Counter(nums)
        tailToCount = collections.defaultdict(lambda: 0)
        for num in nums:
            # if all values of this num are already in subsequences
            if numToCount[num] == 0:
                continue
            
            if numToCount[num] > 0:
                # we can chain the number to an already existing subsequence
                if tailToCount[num-1] > 0:
                    tailToCount[num-1] -= 1
                    tailToCount[num] += 1
                    numToCount[num] -= 1
                else:
                    # we need to make a new list of at least size 3
                    if num+1 in numToCount and numToCount[num+1] > 0 and num+2 in numToCount and numToCount[num+2] > 0:
                        numToCount[num] -= 1
                        numToCount[num+1] -= 1
                        numToCount[num+2] -= 1
                        tailToCount[num+2] += 1
                    else:
                        return False
        return True