import heapq
#numbers_less_than median, median, numbers_greater_than median
#median = if n is odd then maximum value of numbers_less_than median
#median = if n is even then the average of max element of left side and the right side heaps
class MedianFinder:

    def __init__(self):
        self.small = [] #max heap, inverted min heap
        self.large = [] #min heap, we will take out min value out of this side of the numbers

    def addNum(self, num: int) -> None:
        
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))
        

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()