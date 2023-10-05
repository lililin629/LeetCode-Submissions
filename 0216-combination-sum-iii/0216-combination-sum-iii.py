class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # target = n
        ans = []
        self.helper(k, n, 1, [], ans)
        return ans
    
    def helper(self, k, n, num, com, ans):
        if k == 0 and n == 0:
            ans.append(list(com))
            return
        elif k < 0 or n < 0:
            return
        for i in range(num, 10):
            com.append(i)
            self.helper(k-1, n-i, i+1, com, ans)
            com.pop()
        

        