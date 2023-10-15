class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answers = []
        self.dfs(1, n, k, [], answers)
        return answers
    
    def dfs(self, start, n, k, ans, answers):
        if len(ans) == k:
            answers.append(sorted(list(ans)))
            return
        
        for i in range(start, n+1):
            ans.append(i)
            self.dfs(i+1, n, k, ans, answers)
            ans.pop()
        
        