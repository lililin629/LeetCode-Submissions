class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        r = len(tokens)-1
        l = 0
        score = 0
        mx_score = 0
#         print(tokens)
        
        while l <= r:
            # print(l)
            # print(r)
            # print('---')
            if power >= tokens[l]:
                score += 1
                mx_score = max(mx_score, score)
                power -= tokens[l]
                l += 1
            
            elif score > 0:
                power += tokens[r]
                score -= 1
                r -= 1
            else:
                break
        return mx_score
        
                
            
        