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

        def recurse(curr_steps):
            if curr_steps > n:
                return 0
            if curr_steps == n:
                return 1

            return recurse(curr_steps + 1) +  \
                    recurse(curr_steps + 2) 

        return recurse(0)