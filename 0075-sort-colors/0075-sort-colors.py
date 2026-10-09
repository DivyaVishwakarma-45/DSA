class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """Do not return anything, modify nums in-place instead."""
        low=0;mid=0;h=len(nums)-1
        while(mid<=h):
            if(nums[mid]==0):
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif(nums[mid]==2):
                nums[h],nums[mid]=nums[mid],nums[h]
                h-=1
            else:
                mid+=1
        