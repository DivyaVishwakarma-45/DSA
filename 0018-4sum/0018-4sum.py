class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        ans=[]
        for i in range(n-3):
            if(i>0 and nums[i]==nums[i-1]): continue
            j=i+1
            while(j<n):
                p=j+1;q=n-1
                while(p<q):
                    sum=nums[i]+nums[j]+nums[p]+nums[q]
                    if(sum>target):
                        q-=1
                    elif(sum<target):
                        p+=1
                    else:
                        ans.append([nums[i],nums[j],nums[p],nums[q]])
                        p+=1;q-=1
                        while(p<q and nums[p]==nums[p-1]):
                            p+=1
                j+=1
                while(j<n and nums[j]==nums[j-1]):j+=1
        return ans
