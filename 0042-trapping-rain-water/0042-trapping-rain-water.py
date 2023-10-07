class Solution:
    def trap(self, height: List[int]) -> int:
        tallest = max(height)
        idx = height.index(tallest) 
        water = 0
        
        max_left = 0
        for i in range(0, idx):
            max_left = max(max_left, height[i])
            water += (max_left-height[i])
        
        max_right = 0
        for j in range(len(height)-1, idx, -1):
            max_right = max(max_right, height[j])
            water += (max_right-height[j])
        return water
            
            
                
                
            
            
            
            
        
        
            
            
        