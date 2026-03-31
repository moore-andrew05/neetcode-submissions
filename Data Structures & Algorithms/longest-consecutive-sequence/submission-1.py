class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_so_far = 0

        for num in nums:
            if (num - 1) in nums:
                continue
            size = 1
            while (num + 1) in nums:
                size += 1
                num += 1

            max_so_far = max(max_so_far, size)

        return max_so_far



        
# nums = [0,3,2,5,4,6,1,1]
# up - {1: 2, 4: 2, 3: 2, 6: 2, 5: 3, 7: 3, 2: 3}
# down - {-1: 2, 2: 2, 1: 3, 4: 2, 3: 3, 5: 2, 0: 4}