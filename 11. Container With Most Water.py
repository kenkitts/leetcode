
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



height = [2,3,4,5,18,17,6]
solution = Solution()
print(solution.maxArea(height))