class Solution:
    

    
    
    def rotate(self, nums: List[int], k: int) -> None:
        k= k%len(nums)
       
        def rev(nums: List[int],i: int, j: int):

            while(i<=j and i<len(nums) and j < len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j-=1
            print(nums)

        rev(nums,0,len(nums)-1)
        rev(nums,0,k-1)
        rev(nums,k,len(nums)-1)



        