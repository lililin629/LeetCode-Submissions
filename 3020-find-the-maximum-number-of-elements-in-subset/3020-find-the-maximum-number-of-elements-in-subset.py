class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        d = Counter(nums)
        max_l = 1
        if 1 in d and d[1] > 1:
            if d[1] % 2 == 1:
                max_l = d[1]
            else:
                max_l = d[1] - 1
        
        for key in d:
            if d[key] > 1 and key > 1:
                max_l = max(self.dfs(d, key, 1), max_l)
        return max_l
    
        
    def dfs(self, d, key, cur_l):
        nex = key**2
        if nex in d and d[nex] > 1:
            return self.dfs(d, nex, cur_l+2)
        elif nex in d and d[nex] <= 1:
            return cur_l + 2
        else:
            return cur_l
            
        