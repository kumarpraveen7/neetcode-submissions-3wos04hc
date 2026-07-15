class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0
        nums = sorted(set(nums))
        d = dict()
        maxc = 1
        for i in nums:
            if(i-1 in d):
                d[i] = d[i-1] + 1
                maxc = max(maxc,d[i])
            else:
                d[i] = 1
        return maxc
        