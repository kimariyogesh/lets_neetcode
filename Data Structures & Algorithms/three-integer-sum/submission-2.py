class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        res = []
        while i < len(nums)-2:
            if i>0 and nums[i] == nums[i-1]:
                i+=1
                continue

            target = - nums[i]
            j = i+1
            k = len(nums)-1
            while j<k:
                if target == nums[j] + nums[k]:
                    res.append([nums[i], nums[j], nums[k]])
                    j_val = nums[j]
                    while j<k and nums[j] == j_val:
                        j+=1
                    k_val = nums[k]
                    while j<k and nums[k] == k_val:
                        k-=1
                        

                elif target < nums[j] + nums[k]:
                    k-=1
                
                else :
                    j+=1
            i+=1
        return res