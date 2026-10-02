class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow=nums[0];fast=nums[0]
        while True:
            slow=nums[slow] #+1
            fast=nums[nums[fast]] #2
            if(slow == fast):
                break
        slow2=nums[0]
        while(slow != slow2):
            slow=nums[slow]
            slow2=nums[slow2]
        return slow