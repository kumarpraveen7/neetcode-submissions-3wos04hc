class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxs = 0
        i = 0
        tmp = 0
        while(i < len(nums)):

            if(nums[i] == 1):
                tmp+=1
                if(i==len(nums)-1):
                    maxs = max(maxs, tmp)
            else:
                maxs = max(maxs,tmp)
                tmp = 0
            i+=1
        return maxs
        