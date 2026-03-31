class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 2:
            if nums[0] == target:
                return 0
            else:
                return -1

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > target:
                r = mid - 1

            elif nums[mid] < target:
                l = mid + 1

            else:
                return mid

        return -1 