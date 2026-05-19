class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxs = 0
        i = 0
        tmp = 0
        while(i < len(nums)):

            if(nums[i] == 1):
                tmp+=1
            else:
                tmp = 0
            maxs = max(maxs,tmp)
            
            i+=1
        return maxs
        