class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for i in nums:
            if(i in d):
                d[i]+=1
            else:
                d[i] = 1
        
        l = sorted(d.items(), key = lambda x:x[1], reverse = True)
        res = []
        for i in range(k):
            res.append(l[i][0])
        return res