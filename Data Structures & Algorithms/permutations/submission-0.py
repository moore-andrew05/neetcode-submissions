class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ret = []
        def recurse(i, curr_nums, curr_perm):
            if len(curr_perm) == len(nums):
                ret.append(curr_perm)
                return
            
            if i >= len(curr_nums):
                return

            new_nums = curr_nums[:]
            chosen = new_nums.pop(i)
            recurse(0, new_nums, curr_perm[:] + [chosen]) 
            recurse(i + 1, curr_nums, curr_perm)

        recurse(0, nums, [])
        return ret
        


