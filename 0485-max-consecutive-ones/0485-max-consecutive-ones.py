class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        freq=0;ans=1;mx = 0
        for i in nums:
            if(ans == i):
                freq+=1
            else:
                mx = max(freq,mx)
                freq = 0
        return max(freq,mx)