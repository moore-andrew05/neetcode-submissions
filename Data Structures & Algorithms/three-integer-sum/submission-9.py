class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []

        for i, a in enumerate(sorted_nums):

            if a > 0:
                break

            if i > 0 and a == sorted_nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while r > l:
                cur_sum = sorted_nums[l] + sorted_nums[r] + a

                if cur_sum > 0: 
                    r -= 1

                elif cur_sum < 0:
                    l += 1

                else:
                    res.append([a, sorted_nums[l], sorted_nums[r]])
                    l += 1
                    r -= 1
                    while sorted_nums[l] == sorted_nums[l - 1] and l < r:
                        l += 1

        return res
