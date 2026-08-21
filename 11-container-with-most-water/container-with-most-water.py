class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,area,j=0,0,len(height)-1
        while i<j:
            area1=(j-i)*min(height[i],height[j])
            area=max(area1,area)
            if  height[i]>height[j]:j-=1
            else:i+=1
        return area