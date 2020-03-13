"""
Motivation:
The problem can be broken into two parts: 1) finding the next greater element for each element in
nums2, and 2) creating the solution by assigning the proper next greater element for the elements
in nums1.
For the first part of the problem, for any element in nums2, its next greater can be found by 
looping through the rest of the array until we find the next greater element (or reach the end and
assign its next greater as -1). To do this for all the elements in nums2 would take quadratic time 
since you'd index the array len(nums2)*(len(num2)+1)//2 times. Interestingly, this can actually be 
done in linear time with the use of a stack. If we instead shift our perspective of the problem 
from "what is the next greater element for this element in nums2" to "this element in nums2 is the
next greater element for which elements before it," then it may be a little clearer that the 
solution can be found through a monotonically decreasing stack. Take the following array as an 
example for nums2: [9,3,2,1,5,6,4] and apply the following strategy:
1) as you iterate through the array, if the stack isn't empty, check if the top of the stack is 
greater or less than the current element. If it's greater, then you haven't found the next greater 
element for any element in your stack. if it's less, then you've the current element you are 
considering in the array is the next greater element for all elements in your stack that are less 
than it. Thankfully since the stack is monotonically decreasing, all your valid solutions will be 
at the top of the stack!
2) add the current element in the array to your stack.
3) once you finish traversing the array, all elements left in your stack do not have a next greater
element.
4) all remaining elements in the stack, have a corresponding "next greater element" of -1
So, by the time you reach the 4th element in nums2 (5), your stack is [9,3,2,1], and you pop off 
the top 3 elements whose next greater element is 5.
The second part of the problem can easily be achieved if we store the next greater element for each
element in nums2 in a dictionary. Then we can easily loop through nums1 and find each of its 
elements corresponding next greater element.

Time Complexity:
The time complexity is linear to the length of arrays since we loop through both arrays once.

Space Complexity:
The space complexity is Linear to the size nums2. In the worst case scenario, the stack is the 
length of nums2 at its largest when the elements of nums2 are monotonically decreasing. The size
of the dictionary is also linear to the size of nums2.
"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # initialize stack and dictionary
        stack = []
        numToNextGreater = {}

        for num in nums2:
            # map the elements in nums2 to their next greater element
            while stack and stack[-1] < num:
                numToNextGreater[stack.pop()] = num
            # have to add the current element in nums2 to the stack to find its next greater later
            stack.append(num)
        # anything left in the stack did not have a next greater, and is by def assigned a next
        # greater of -1
        while stack:
            numToNextGreater[stack.pop()] = -1

        # now we iterate through nums1 and build our solution with our dictionary
        sol = []
        for num in nums1:
            sol.append(numToNextGreater[num])
        return sol