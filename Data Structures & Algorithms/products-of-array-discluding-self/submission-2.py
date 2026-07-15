class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        larr = [1]
        cur = 1
        for i in range(1,len(nums)):
            cur = cur*nums[i-1]
            larr.append(cur)
        cur = 1
        rarr = [1]
        for i in range(len(nums)-1,0,-1):
            cur *= nums[i]
            rarr.append(cur)
        rarr = rarr[::-1]
        for i in range(len(larr)):
            larr[i] *= rarr[i]
        return larr
        print(larr)
        print(rarr)
        return []
        