'''
Given an `int` n

Return:
- `int` distinct ways n can be made with 1 and 2.

for stair:
    base cases:
        if steps taken > height stairs - return 0
        if steps taken == height stairs - return 1
    take 1:
        increment by 1
    take 2:
        increment by 2
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def recurse(curr_steps):
            if curr_steps == 0:
                return 1

            two = 0
            if 2 <= curr_steps:
                if curr_steps - 2 in cache:
                    two = cache[curr_steps - 2]
                else:
                    two = recurse(curr_steps - 2)
                    cache[curr_steps - 2] = two

            if curr_steps - 1 in cache:
                one = cache[curr_steps - 1]
            else:
                one = recurse(curr_steps - 1)
                cache[curr_steps - 1] = one
            return two + one


        return recurse(n)