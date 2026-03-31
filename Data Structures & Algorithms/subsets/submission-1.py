'''

for i in nums:
    choose:


'''


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def get_subsets_from_nums(i, curr_subset):
            if i >= len(nums):
                ret.append(curr_subset)
                return

            get_subsets_from_nums(i + 1, curr_subset=curr_subset[:] + [nums[i]])
            get_subsets_from_nums(i + 1, curr_subset=curr_subset[:])

        get_subsets_from_nums(0, [])
        return ret


        