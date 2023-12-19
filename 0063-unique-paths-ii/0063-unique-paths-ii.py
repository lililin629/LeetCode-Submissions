class Solution:
   
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        self.memo = defaultdict(int)
        
        return self.dfs(0, 0, m, n, obstacleGrid)
       
    
    def dfs(self, cx, cy, m, n, obstacleGrid):
        if (cx, cy) in self.memo:
            return self.memo[(cx, cy)]
        if cx >= m or cy >= n or obstacleGrid[cx][cy] == 1:
            return 0
        if (cx, cy) == (m-1, n-1):
            return 1
        
        
        self.memo[(cx, cy)] = self.dfs(cx+1, cy, m, n, obstacleGrid) + self.dfs(cx, cy+1, m, n, obstacleGrid)
        return self.memo[(cx, cy)]
               
              
                
            
        
        
        
        