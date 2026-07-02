class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_w = 0
        n = len(height)
        i, j = 0, n-1
        # i         | 1 7  7  7
        # j         | 6 6  3  7
        # water     | 7 36 15 28
        # maxwater  | 7 36 36 36
        while i<j:
            wt = min(height[i], height[j]) * (j-i)
            max_w = max(max_w, wt)
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return max_w
