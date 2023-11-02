class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        # 4 <= n <= 12
        # [1-3]*4
        ans = []
        self.dfs(ans, [], s, 0)
        return ans
        
    def dfs(self, ans, ip, s, idx):
        if len(ip) == 4 and idx == len(s):
            sip = '.'.join(ip)
            ans.append(sip)
            return
        
        if len(ip) == 4 and idx != len(s):
            return
        
        for i in range(1,4):
            if idx+i > len(s):
                break
            st = s[idx:idx+i]
            if i > 1 and s[idx] == '0':
                continue
            if int(st) > 255:
                continue
            
            self.dfs(ans, ip+[s[idx:idx+i]], s, idx+i)
           
        
        
        
        
        
        
        
    
        
        