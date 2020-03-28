"""
Motivation:
The key here is to observe that the majority element is one that appears more than n/2 times, as
opposed to the most frequent element in the list. For instance, take the following two lists of 
size 6: [1,2,3,4,5,5] and [1,1,1,2,3,4]. The second array has a majority element while the first
does not. This means that the sum of numbers that are not in the majority will never exceed the
majority element, so we can take the following strategy:
1) select the first element as your candidate
2) as you iterate through the array, if the current element matches your candidate, increment count
3) if it does not match, then decremement count. If count < 0, the current element becomes the 
new candidate.
Since the majority element will always be equal or greater than the rest of the elements in the 
array, your candidate will always be the majority element after looping through the array.

Time Complexity:
The time complexity is linear to the length of the array since we loop through it once.

Space Complexity:
The space complexity is O(1). As the size of the input grows, the amount of memory we need for the 
algorithm does not grow.
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # check that the array is indexable
        if len(nums) == 0:
            return
        # initialize candidate
        candidate = nums[0]
        # count represents the number of times we've seen the element so far
        count = 1 
        # loop through rest of the array
        for num in nums[1:]:
            if num == candidate:
                count += 1
            else:
                count -= 1
                # if the count is less than 0, then for the part of the array that's been traversed
                # so far, the current candidate cannot be the majority element
                if count < 0:
                    count = 1
                    candidate = num
        return candidate