class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        
        for point in points:
            dist = math.sqrt((point[0]) ** 2 + point[1] ** 2)
            min_heap.append((dist, point))

        res = []
        heapq.heapify(min_heap)

        for _ in range(k):
            res.append(heapq.heappop(min_heap)[1])

        return res
