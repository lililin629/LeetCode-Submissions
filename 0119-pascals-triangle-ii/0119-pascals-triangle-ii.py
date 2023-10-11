class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        ans = []
        pre = self.getRow(rowIndex-1)
        for i in range(rowIndex+1):
            if i == 0 or i == rowIndex:
                ans.append(1)
            else:
                ans.append(pre[i-1] + pre[i])
        return ans
            
        