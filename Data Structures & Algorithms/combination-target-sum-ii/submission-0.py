class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, subset, cur_sum):

            if cur_sum == target:
                res.append(subset[::])
                return

            if i >= len(candidates) or cur_sum > target:
                return

            subset.append(candidates[i])
            cur_sum += candidates[i]
            backtrack(i + 1, subset, cur_sum)

            cur_sum -= subset.pop()

            while (i < len(candidates) - 1) and (candidates[i] == candidates[i + 1]):
                i += 1

            backtrack(i + 1, subset, cur_sum)


        backtrack(0, [], 0)
        return res
