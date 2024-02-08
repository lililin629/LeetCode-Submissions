class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        d = defaultdict(list)
        
        for c in s:
            d[c] = [len(s)-1, 0]
            
        for i, c in enumerate(s):
            d[c] = [min(d[c][0], i), max(d[c][1], i)]
        
        # lst = [(start, end, c)]
        lst = []
        for c in d:
            lst.append((d[c][0], d[c][1], c))
        lst.sort(reverse= True)
        st = []
        
        ans = []
       
        start, end, c = lst.pop()
        st.append((start, end, c))
        while lst:
            ns, ne, nc = lst.pop()
            if ns > st[-1][1]:
                ans.append(ns-st[0][0])
                st = []
                st.append((ns, ne, nc))
            elif ne > st[-1][1]:
                st.append((ns,ne,nc))
        ans.append(st[-1][1]-st[0][0] + 1)
        return ans
                
                
                
                
                
            
            
        