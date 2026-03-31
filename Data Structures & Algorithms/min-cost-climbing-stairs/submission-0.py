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

        def recurse(i):
            if i >= len(cost):
                return 0

            one = recurse(i + 1)
            two = recurse(i + 2)

            return cost[i] + min(one, two)

        return min(recurse(0), recurse(1))
        