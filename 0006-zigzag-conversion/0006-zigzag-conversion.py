class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        team = 2*numRows-2
        ids = []
        rows = defaultdict(list)
        
        # create row id's for each member in the team
        for i in range(numRows):
            ids.append(i)
        for i in range(numRows-2,0,-1):
            ids.append(i)
        
        
        for i in range(len(s)):
            idx = i%team
            row_id = ids[idx]
            rows[row_id].append(s[i])
        
        ans = ''
        for row in rows:
            s = ''.join(rows[row])
            ans += s
        return ans
                
        