class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        ans = ''
        if s[0] == '-':
            s = s[1:]
            for ch in s[::-1]:
                ans += ch
            ans = -int(ans)
        else:
            for ch in s[::-1]:
                ans += ch
            ans = int(ans)
        if ans > 2**31-1 or ans < -(2**31):
            return 0
        return ans
            
       
            
       
            
        