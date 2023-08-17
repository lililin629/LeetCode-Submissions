class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = defaultdict(list)
        for i, [top, under] in enumerate(equations):
            d[top].append((under, values[i]))
            d[under].append((top, 1/values[i]))
        
        self.d = d
        self.answers = []
        
        for [src, des] in queries:
            self.visited = set()
            self.ans = -1
            self.dfs(src, des, 1)
            self.answers.append(self.ans)
        return self.answers
        
    def dfs(self, src, des, cur_num):
        if src not in self.d or des not in self.d:
            return
        if src == des:
            self.ans = cur_num
            return
        self.visited.add(src)
        for nei, mul in self.d[src]:
            if nei not in self.visited:
                self.dfs(nei, des, cur_num*mul)
        
       
            
            
        