class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-1 * num for num in nums]
        heapq.heapify(maxHeap)

        last_num = None
        while k > 0:
            curr_num = heapq.heappop(maxHeap)
            if last_num is not None and curr_num == last_num:
                continue
            k -= 1

        return -1 * curr_num



        