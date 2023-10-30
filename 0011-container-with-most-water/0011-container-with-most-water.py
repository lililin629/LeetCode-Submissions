class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        mx_area = 0
        
        while l < r:
            mx_area = max(mx_area, min(height[l], height[r])*(r-l))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return mx_area
            
        