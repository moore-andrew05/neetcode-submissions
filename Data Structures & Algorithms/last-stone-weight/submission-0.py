class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-val for val in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)

            if stone1 == stone2:
                continue

            if stone2 < stone1:
                heapq.heappush(max_heap, -(stone1 - stone2))
            
        if len(max_heap) == 1:
            return -heapq.heappop(max_heap)

        else:
            return 0
