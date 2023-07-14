class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = []
        
        for ls in matrix:
            for c in ls:
                m.append(c)
        
        if len(m) < 1:
            return False
        
        
        s = 0
        e = len(m) - 1
        while s + 1 < e:
            mid = (s + e) // 2 
            if m[mid] == target:
                return True
            if m[mid] < target:
                s = mid
            if m[mid] > target:
                e = mid
        if m[s] == target:
            return True
        if m[e] == target:
            return True
        return False
        