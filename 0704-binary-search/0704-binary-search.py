class Solution:
    def bs(self,nums,target,st,end):
        if(st<=end):
            mid=st+(end-st)//2
            if(nums[mid] == target):
                return mid
            elif(nums[mid]>target):
                return self.bs(nums,target,st,mid-1)
            else:
                return self.bs(nums,target,mid+1,end)
        return -1
    def search(self, nums: list[int], target: int) -> int:
        st=0;end=len(nums)-1
        return self.bs(nums,target,st,end)