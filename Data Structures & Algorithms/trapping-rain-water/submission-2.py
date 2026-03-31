class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) == 1:
            return 0


        l = 0
        r = len(height) - 1

        max_l = height[l]
        max_r = height[r]

        res = 0
        test = []

        while l < r:
            if max_l <= max_r:
                l += 1
                res += max(max_l - height[l], 0)
                test.append((f'l={l}, val={max(max_l - height[l], 0)}'))
                if height[l] > max_l:
                    max_l = height[l]

            elif max_r < max_l:
                r -= 1
                res += max(max_r - height[r], 0)
                test.append((f'r={r}, val={max(max_r - height[l], 0)}'))
                if height[r] > max_r:
                    max_r = height[r]

        print(test)
        return res




