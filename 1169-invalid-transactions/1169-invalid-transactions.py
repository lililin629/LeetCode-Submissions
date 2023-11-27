class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactions.sort(key = lambda t: int(t.split(',')[1])) # sort by time
        ans = set()
        d = defaultdict(deque) # {name: {(time, location, idx)}}
        
        for i in range(len(transactions)):
            [name, time, amt, city] = transactions[i].split(',')
            q = d[name]
            if int(amt) > 1000:
                ans.add((transactions[i], i))
            while q and (int(time) - q[0][0]) > 60:
                q.popleft()
            
            for t, c, j in q:
                if c != city:
                    ans.add((transactions[i], i))
                    ans.add((transactions[j], j))
                    
            d[name].append((int(time), city, i))
        
        ret = list(t for (t, idx) in ans)
        return ret
        
       
            
            
        
        
            
                
        

        