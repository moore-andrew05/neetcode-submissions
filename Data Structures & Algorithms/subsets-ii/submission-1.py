'''
Maybe the same as subset but we append every time we take.

'''


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        nums.sort()

        def recurse(i, curr_set):
            if i >= len(nums):
                return

            curr_set.append(nums[i])
            ret.append(curr_set[:])
            recurse(i + 1, curr_set)
            curr_set.pop()

            curr_num = nums[i]
            while i <= len(nums) - 1 and nums[i] == curr_num:
                i += 1
            recurse(i, curr_set)

        recurse(0, [])
        return ret


        