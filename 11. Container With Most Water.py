class Solution:
    def maxArea(self, height) -> int:
        l, r, max_water = 0, len(height)-1, 0
        while l < r:
            max_water = max(max_water, (r-l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_water