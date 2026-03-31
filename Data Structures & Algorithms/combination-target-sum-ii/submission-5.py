
'''
array of `int` candidates
- may contain dupes

`int` target

return list[list[int]]
- **unique** combinations of candidates
- sum == target
- any order for both lists
- no repeats of candidates[i]


curr_sum = 0
curr_comb = []
i = 0

for i in len(candidates):
    base cases:
        if curr_sum > target or i >= len(candidates)
            give up (return without appending)
        if curr_sum == target:
            append and return
        

    choose:
        curr_comb add candidate[i]
        advance i
        advance curr_sum

    skip:
        advance i


^ This works but gives dupes. Sorting?

If candidates is sorted, we are guaranteed to encounter duplicates in order, but how does this help.
consider extreme case:
candidates = [1, 1, 1, 1, 1, 1, 1, 1...]
target = 3

answer = [1, 1, 1]


'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()

        def recurse(i, curr_sum, curr_comb):
            if curr_sum == target:
                ret.append(curr_comb[:])
                return

            if curr_sum > target or i >= len(candidates):
                return

            curr_comb.append(candidates[i]) 
            recurse(i + 1, curr_sum + candidates[i], curr_comb)
            curr_comb.pop()

            curr_num = candidates[i]
            while i <= len(candidates) - 1 and candidates[i] == curr_num:
                i += 1
            recurse(i, curr_sum, curr_comb)

        recurse(0, 0, [])
        return ret
            

        
