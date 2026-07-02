class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # n = len(heights)
        # vol = 0
        # for i in range(0,n):
        #     for j in range(i+1,n):
        #         vol = max(vol, min(heights[i], heights[j]) * (j-i))
        # return vol

        # Two pointers
        n = len(heights)
        l,r = 0, n-1
        res = 0

        while l<r:
            area = min(heights[l],heights[r]) * (r-l)
            res = max(res, area)

            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return res