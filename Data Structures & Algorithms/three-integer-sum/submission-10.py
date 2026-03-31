class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = 0 
        r = len(nums) - 1

        ret = []

        while l < len(nums) - 1:
            while r > l:
                for mid in range(l + 1, r):
                    if nums[l] + nums[mid] + nums[r] == 0:
                        item = sorted([nums[l], nums[mid], nums[r]])
                        if item not in ret:
                            ret.append(item)

                r -= 1

            r = len(nums) - 1
            l += 1

        return ret
