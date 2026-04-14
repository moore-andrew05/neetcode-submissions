class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i, num in enumerate(nums):
            needed = target - num
            if needed in visited:
                return [visited[needed], i]

            visited[num] = i

        return -1

        