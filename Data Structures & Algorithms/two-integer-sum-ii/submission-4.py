class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while r > l:
            curr_sum = numbers[l] + numbers[r]

            if curr_sum > target:
                r -= 1
                continue

            if curr_sum < target:
                l += 1
                continue

            return [l + 1, r + 1]