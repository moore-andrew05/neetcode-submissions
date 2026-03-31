class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1 for _ in range(len(nums))]
        suffixes = [1 for _ in range(len(nums))]

        running_product = 1
        for i in range(1, len(nums)):
            running_product *= nums[i - 1]
            prefixes[i] = running_product

        running_product = 1
        for i in range(len(nums) - 2, -1, -1):
            running_product *= nums[i + 1]
            suffixes[i] = running_product


        return [i * k for i, k in zip(prefixes, suffixes)]
            
            