class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums);sum=0
        esum=(n*(n+1))//2
        for i in nums:
            if( i== 0):
                continue
            else:
                sum=sum+i
        ans = esum-sum
        return ans