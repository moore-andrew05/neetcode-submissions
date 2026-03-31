class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        for i, _ in enumerate(heights):

            l = i
            r = len(heights) - 1

            while l < r:
                area = min(heights[l], heights[r]) * (r - l)
                if area > max_water:
                    max_water = area

                r -= 1

        return max_water