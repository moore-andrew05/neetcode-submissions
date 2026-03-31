'''
array of distinct integers: nums
target integer: target

unique combinations of nums where sum == target

numbers can repeat.


'''
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []

        def recurse(i, curr_sum, curr_seq):
            if curr_sum > target:
                return
            if curr_sum == target:
                ret.append(curr_seq[:]) 
                return

            if i >= len(nums):
                return

            curr_seq.append(nums[i])
            recurse(i, curr_sum + nums[i], curr_seq)
            curr_seq.pop()
            recurse(i + 1, curr_sum, curr_seq)


        recurse(0, 0, [])
        return ret
        