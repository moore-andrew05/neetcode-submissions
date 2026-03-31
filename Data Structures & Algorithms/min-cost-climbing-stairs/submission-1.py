'''
array of 'int'

can start at 0 or 1

traverse the array in steps of 1 or 2 with min cumulative sum

while i < len(cost):
    step 1:


    step 2:


     



'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}

        def recurse(i):
            if i >= len(cost):
                return 0

            if i in cache:
                return cache[i]

            one = recurse(i + 1)
            two = recurse(i + 2)
            chose = min(one, two)
            cache[i] = cost[i] + chose

            return cost[i] + chose

        return min(recurse(0), recurse(1))
        