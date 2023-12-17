class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            ds = Counter(s)
            st = ''
            for c, count in sorted(ds.items()):
                st += str(count)
                st += c
            d[st].append(s)
        
        ans = []
        for st, lst in d.items():
            ans.append(lst)
        return ans
                
            
        
        