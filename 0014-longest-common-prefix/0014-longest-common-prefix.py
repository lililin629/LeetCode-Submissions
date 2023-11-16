class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        min_len = float('inf')
        min_word = ''
        for word in strs:
            if len(word) < min_len:
                min_len = len(word)
                min_word = word
        if min_len == 0:
            return ''
        
        for i in range(min_len):
            for word in strs:
                if word[i] != min_word[i]:
                    return min_word[:i]
        return min_word
                    
         

                
        