class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr = arr[::-1]
        res = []

        maxs = None

        i = 0
        while(i<len(arr)):
            if(maxs==None):
                maxs = arr[i]
                res.append(-1)
            
            else:
                maxs = max(maxs,arr[i-1])
                res.append(maxs)
            
            i+=1
        
        return res[::-1]
            
            
            