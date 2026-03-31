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
            if curr_steps == 0:
                return 1

            two = 0
            if 2 <= curr_steps:
                two = recurse(curr_steps - 2)

            one = recurse(curr_steps - 1)
            return two + one


        return recurse(n)