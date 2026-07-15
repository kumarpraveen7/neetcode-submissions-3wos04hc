class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        larr = [1]
        cur = 1
        [1,2,4,6]
        [1,1,2,8]
        [48,24,6,1]
        for i in range(1,len(nums)):
            cur = cur*nums[i-1]
            larr.append(cur)
        cur = 1
        for i in range(len(nums)-1,0,-1):
            larr[i] *= cur
            cur *= nums[i]
            

        
        larr[0]*= cur
        print(larr)
        return larr
        # rarr = rarr[::-1]
        # for i in range(len(larr)):
        #     larr[i] *= rarr[i]
        # return larr
       
        