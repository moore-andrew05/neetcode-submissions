class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclidean_distance(x1: int, y1: int, x2: int, y2: int) -> float:
            return math.sqrt((x1 - x2)**2 + (y1-y2)**2) 

        def euclidean_distance_to_origin(x: int, y: int) -> float:
            return euclidean_distance(x, y, 0, 0)

        minHeap = []
        for point in points:
            dist = euclidean_distance_to_origin(*point)
            minHeap.append([dist, point])

        heapq.heapify(minHeap)
        ret = []
        for _ in range(k):
            _, point = heapq.heappop(minHeap)
            ret.append(point)
        
        return ret


