class Solution:
    def reorganizeString(self, s: str) -> str:
        d = defaultdict(int)
        for ch in s:
            d[ch] += 1
        heap = []
        
        for ch, count in d.items():
            heapq.heappush(heap, (-1*count, ch))
        ans = '1'
        while heap:
            cur_count, cur_ch = heapq.heappop(heap)
            ncount, nch = 0, ''
            if heap:
                ncount, nch = heapq.heappop(heap)
            # print(nch)
            # print(ncount)
            # print(ans[-1])
            if ans[-1] == cur_ch or cur_ch == nch:
                return ""
            ans += cur_ch
            ans += nch
            cur_count += 1
            ncount += 1
            if cur_count < 0:
                heapq.heappush(heap, (cur_count, cur_ch))
            if ncount < 0:
                heapq.heappush(heap, (ncount, nch))
        return ans[1:]
                
        
      
        
            
        
        