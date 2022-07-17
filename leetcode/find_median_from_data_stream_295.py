class MedianFinder:

    def __init__(self):
        small, large = [], []
        self.small, self.large = small, large

    def addNum(self, num: int) -> None:
        #max heap
        heapq.heappush(self.small, -num)
        #make sure every num small i s <= every num in large
        if (self.small and self.large and (-self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # uneven size
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = -heapq.heappop(self.large)
            heapq.heappush(self.small, val)


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.small) < len(self.large):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()