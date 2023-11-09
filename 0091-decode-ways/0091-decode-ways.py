class Solution:
    def numDecodings(self, s: str) -> int:
        # invalid: > 26, 0, starts with 0
        # xxx12
        # xxx79
        # xxx10
        # xxx01
        # xxx00
        dp = defaultdict(int)
        n = len(s)
        if s[0] == '0':
            return 0
        dp[0] = 1
        if n > 1:
            if self.valid(s[1]) and self.valid(s[:2]):
                dp[1] = 2
            elif self.valid(s[1]) or self.valid(s[:2]):
                dp[1] = 1
            else:
                dp[1] = 0
        
        for i in range(2, len(s)):
            
            if self.valid(s[i]) and self.valid(s[i-1]) and self.valid(s[i-1:i+1]):
                dp[i] = dp[i-1] + dp[i-2]
            elif self.valid(s[i]) and self.valid(s[i-1]): #79
                dp[i] = dp[i-1]
            elif self.valid(s[i-1]) and self.valid(s[i-1:i+1]): #10
                dp[i] = dp[i-2]
            elif self.valid(s[i]) and not self.valid(s[i-1]) and not self.valid(s[i-1:i+1]): #01
                dp[i] = dp[i-1]
            else:
                dp[i] = 0
        print(dp)
        
        return dp[n-1]
    def valid(self, s1):
        # invalid: > 26, 0, starts with 0
        if s1[0] == '0':
            return False
        if int(s1) > 26:
            return False
        if int(s1) == 0:
            return False
        return True

            # elif int(s[i-1]) == 0 and int(s[i]) == 0: #00
            #     dp[i] = 0
            # elif not valid(s[i]) and not valid(s[i-1:i+1]): #30
            #     dp[i] = 0
            # elif not valid(s[i-1]) and not valid(s[i-1:i+1]): #01
            #     dp[i] = dp[i-1]
