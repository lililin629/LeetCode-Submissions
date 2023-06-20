class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort every string
        ans = []
        strs_map = {}
        for s in strs:
            ls = []
            tp = tuple()
            for ch in s:
                ls.append(ch)
                ls.sort()
                tp = tuple(ls)
            if tp not in strs_map:
                strs_map[tp] = [s]
            else:
                strs_map[tp].append(s)
        for tp in strs_map:
            ans.append(strs_map[tp])
        return ans
                
                
            
            
        
        