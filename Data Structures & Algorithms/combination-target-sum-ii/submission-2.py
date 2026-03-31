'''
array of candidates
no dupes
target int

return all unique combinations of candidates where sum == target
Each candidate used at most once.
Any order

base cases:
    sum > target | i >= len(combinations) -> throw out
    sum == target -> append to solution

for candidate in candidates:
    take:
        add candidate to current subset
        increment current sum
        advance i
    skip:
        advance i 

'''


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates = sorted(candidates)
        def recurse(i, curr_sum, curr_subset):
            if curr_sum > target:
                return
            if curr_sum == target:
                ret.append(curr_subset[:]) if curr_subset not in ret else None
                return
            if i >= len(candidates):
                return

            curr_subset.append(candidates[i])
            recurse(i + 1, curr_sum + candidates[i], curr_subset)
            curr_subset.pop()
            recurse(i + 1, curr_sum, curr_subset)

        recurse(0, 0, [])
        return ret

        