class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        sorted_counts = sorted(counts.items(), key=lambda x: x[1])
        return [i[0] for i in sorted_counts[len(sorted_counts) - k:]]
        