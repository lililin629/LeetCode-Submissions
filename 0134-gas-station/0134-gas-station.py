class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # invariant: prefixSum of gas has to always be greater than prefixSum of cost
        n = len(gas)
        dg = defaultdict(int)
        dc = defaultdict(int)
        ps_gas = ps_cost = dg[-1] = dc[-1] = 0
        
        start = -1
        
        for i in range(n):
            ps_gas += gas[i]
            ps_cost += cost[i]
            dg[i] = ps_gas
            dc[i] = ps_cost
            
            while (dg[i] - dg[start]) < (dc[i] - dc[start]):
                start += 1
            
        if dg[n-1] - dc[n-1] < 0:
            return -1
        return start+1
                
        
        