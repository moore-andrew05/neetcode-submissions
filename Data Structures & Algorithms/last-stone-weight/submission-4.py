class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-1 * stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            stone1 = -1 * heapq.heappop(maxHeap)
            stone2 = -1 * heapq.heappop(maxHeap)

            if stone1 == stone2:
                continue

            heapq.heappush(maxHeap, -1 * abs(stone1 - stone2))
        
        if len(maxHeap) == 1:
            return -1 * maxHeap[0]
        return 0