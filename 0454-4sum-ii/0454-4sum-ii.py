class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        # build a dict for sum(num1, num2) - {(sum, count),...}
        d12 = self.build_d(nums1, nums2)
                
        # iterate dict, for each sum, how many counts of nums3 +nums4 == -sum
        d34 = self.build_d(nums3, nums4)
        
        count = 0
        for s1 in d12:
            if -s1 in d34:
                count += d12[s1]*d34[-s1]
            # for s2 in d34:
            #     if (s1 + s2) == 0:
            #         count += d12[s1]*d34[s2]
        return count
        
        
    def build_d(self, l1, l2):
        d = {}

        for i in l1:
            for j in l2:
                sum12 = i+j
                d[sum12] = d.get(sum12, 0)+1
        return d
        
        