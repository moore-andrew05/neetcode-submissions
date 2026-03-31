'''
list[int] nums

max of set of indices with no adjacent indices


for each house:
    base case:
        i >= len(nums):
            return 0

    last house robbed?

        can't rob house, return 0 + recursion
    memoization:
        if i in cache:
            return cache[i]

    rob:
        return nums[i] + recursion

    don't rob:
        return 0 + recursion


Notes:
- Memoization has to come after the check for if last house was robbed. Why? 
    - Because the cache for that index may have robbed that house, which is invalid.

'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def recurse(i, robbed):
            if i >= len(nums):
                return 0

            if robbed:
                return 0 + recurse(i + 1, False)

            if i in memo:
                return memo[i]

            rob = nums[i] + recurse(i + 1, True)
            norob = 0 + recurse(i + 1, False) 
            memo[i] = max(rob, norob)
            #return max(rob, norob) 
            return memo[i] 

        return recurse(0, False)


        