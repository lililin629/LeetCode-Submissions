class Solution:
    def intToRoman(self, num: int) -> str:
        #3999
        ms = cs = ds = ss = ''
        s = num%10
        if s < 4:
            ss = 'I'*s
        if s == 4:
            ss = 'IV'
        if s == 5:
            ss = 'V'
        if  5 < s < 9:
            ss = 'V'+'I'*(s-5)
        if s == 9:
            ss = 'IX'
        
        d = (num//10)%10
        if d < 4:
            ds = 'X'*d
        if d == 4:
            ds = 'XL'
        if d == 5:
            ds = 'L'
        if  5 < d < 9:
            ds = 'L'+'X'*(d-5)
        if d == 9:
            ds = 'XC'
        
        c = (num//100)%10
        if c < 4:
            cs = 'C'*c
        if c == 4:
            cs = 'CD'
        if c == 5:
            cs = 'D'
        if  5 < c < 9:
            cs = 'D'+'C'*(c-5)
        if c == 9:
            cs = 'CM'
        
        m = (num//1000)%10
        ms = 'M'*m
        
        return ms+cs+ds+ss
        
        
        
        