class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
       num=0
       for i in digits:
            num=num*10+i
       num =  num+1
       digits = [int(x) for x in str(num)]
       return digits