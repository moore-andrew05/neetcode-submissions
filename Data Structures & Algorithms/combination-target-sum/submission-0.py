class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, cur, total):
            
            if cur == total:
                res.append(subset.copy())
                return

            if i >= len(nums) or cur > total:
                return


            cur += nums[i]
            subset.append(nums[i])
            dfs(i, cur, target)

            cur -= subset.pop()
            dfs(i + 1, cur, target)

        dfs(0, 0, target)
        return res