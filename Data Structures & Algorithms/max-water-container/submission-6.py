class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def getArea(bar1, bar2, distance):
            return min(bar1, bar2) * distance

        l = 0 
        r = len(heights) - 1
        curr_max = 0

        while r > l:
            curr_area = getArea(heights[l], heights[r], r - l)
            if curr_area > curr_max:
                curr_max = curr_area

            if heights[r] >= heights[l]:
                l += 1
                continue

            r -= 1

        return curr_max 

