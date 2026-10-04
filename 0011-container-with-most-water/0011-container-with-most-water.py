class Solution:
    def maxArea(self, height: List[int]) -> int:
        lp=0;rp=len(height)-1;maxarea=0
        while lp<rp:
            maxarea = max(maxarea,min(height[lp],height[rp])*(rp-lp))
            if( height[lp]<height[rp]) :lp+=1
            else:rp-=1
        return maxarea