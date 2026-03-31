'''


'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        def recurse(i, robbed, first_robbed):
            if i >= len(nums):
                return 0
            if robbed:
                return 0 + recurse(i + 1, False, first_robbed)

            if i == 0:
                if first_robbed:
                    return nums[i] + recurse(i + 1, True, first_robbed)
                return 0 + recurse(i + 1, False, first_robbed)
            elif i == len(nums) - 1:
                if first_robbed:
                    return 0
                return nums[i]

            if i in memo:
                return memo[i]

            rob = nums[i] + recurse(i + 1, True, first_robbed)
            norob = 0 + recurse(i + 1, False, first_robbed) 
            memo[i] = max(rob, norob)
            return memo[i] 

        memo = {}
        rob_first = recurse(0, False, True)
        memo = {}
        norob_first = recurse(0, False, False)

        return max(rob_first, norob_first)
        