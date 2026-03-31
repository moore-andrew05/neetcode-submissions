class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            val = nums[mid]
            
            if val > target:
                r = mid - 1

            elif val < target:
                l = mid + 1

            else:
                return mid

        return -1
            