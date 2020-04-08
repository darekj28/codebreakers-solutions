from heapq import heappush, heappop
class MedianFinder:
    # all operations are O(1) in both time and space
    def __init__(self):
        """
        initialize your data structure here.
        """
        # holds numbers larger and equal to the median
        self.largerHalf = [] 
        # holds numbers less than the median
        # note that all elements in the smallerHalf will be multiplied by -1 since python heaps are min heaps
        self.smallerHalf = []
        # keeps track of the quantity of numbers we've seen
        self.count = 0

    def addNum(self, num: int) -> None:
        if self.count % 2 == 0:
            # we want to increase the size of the largerHalf heap by 1
            if self.count == 0 or num > -self.smallerHalf[0]:
                heappush(self.largerHalf, num)
            else:
                # the new number belongs to the smallerHeap, so we need to move the largest number in the smallerHeap to the largerHeap and the new number to the smallerHeap
                heappush(self.largerHalf, -heappop(self.smallerHalf))
                heappush(self.smallerHalf, -num)
        else:
            # we want to increase the size of the smallerHeap by 1
            if num < self.largerHalf[0]:
                heappush(self.smallerHalf, -num)
            else:
                # the new number belongs in the largerHeap, so we need to move the smallest element in the largerHeap to the smallerHeap and the new number to the largerHeap
                heappush(self.smallerHalf, -heappop(self.largerHalf))
                heappush(self.largerHalf, num)
        # increment total quantity of numbers in our heaps
        self.count += 1
        
    def findMedian(self) -> float:
        if self.count % 2 == 1:
            # median is in the largerHalf heap
            return self.largerHalf[0]
        else:
            # median is the average of values in both heaps
            return (self.largerHalf[0] - self.smallerHalf[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()