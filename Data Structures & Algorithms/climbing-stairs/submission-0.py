'''
You are given an integer n representing the number of steps to reach the top of a staircase.

You can climb with either 1 or 2 steps at a time.

Taking 1 step or 2 always decreases the number of steps left

Return the number of permutations
112 = 4
211 = 4
are distinct

1 <= n <= 30
'''

class Solution:
    def climbStairs(self, n: int) -> int:

        def num_permutations_of_n(steps: int) -> int:

            if steps == 0:
                return 1
            two = 0
            if 2 <= steps:
                two = num_permutations_of_n(steps - 2)
            one = num_permutations_of_n(steps-1)
            return two + one

        return num_permutations_of_n(n)
        