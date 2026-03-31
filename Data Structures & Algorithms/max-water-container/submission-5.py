class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            water = (r - l) * min(heights[r], heights[l])
            print(heights[l], heights[r])

            if water > max_water:
                max_water = water

            if heights[r] >= heights[l]:
                l += 1
            else:
                r -= 1


        return max_water