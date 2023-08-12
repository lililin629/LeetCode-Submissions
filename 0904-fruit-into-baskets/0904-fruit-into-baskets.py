class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        r = 0
        d = defaultdict(int)
        d[fruits[l]] += 1
        count = 1
        max_count = 0
        
        
        while r < len(fruits):
            
            if len(d) <= 2:
                r += 1
                if r < len(fruits):
                    d[fruits[r]] += 1
                    count += 1
                   
            if len(d) > 2:
                d[fruits[l]] -= 1
                count -= 1
                
                if d[fruits[l]] == 0:
                    del d[fruits[l]]
                l += 1
            max_count = max(max_count, count)
        return max_count
                
                
            