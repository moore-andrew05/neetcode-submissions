class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        # Initial Addition
        if not self.min_heap and not self.max_heap:
            med = 0
        else:
            med = self.findMedian()
        if num > med:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, num * -1)
        # Rebalance
        if len(self.min_heap) - len(self.max_heap) > 1:
            heapq.heappush(
                self.max_heap,
                -1 * heapq.heappop(self.min_heap
            ))
        if len(self.max_heap) - len(self.min_heap) > 1:
            heapq.heappush(
                self.min_heap,
                -1 * heapq.heappop(self.max_heap
            ))
        

    def findMedian(self) -> float:
        if not self.min_heap or not self.max_heap:
            return self.min_heap[0] if self.min_heap else self.max_heap[0]

        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            return (self.min_heap[0] + -1*self.max_heap[0]) / 2

        else:
            return self.min_heap[0] if len(self.min_heap) > len(self.max_heap) else -1 * self.max_heap[0]