import sys
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums_set = set(nums)
        # nums_arr = list(nums_set)
        # nums_arr.sort()
        # res = 1 
        # maxi = 1
        # if len(nums) == 0:
        #     return 0
        #     sys.exit()
        # for i in range(len(nums_arr)-1):
        #     if nums_arr[i]+1 == nums_arr[i+1]:
        #         res+=1 
        #         maxi = max(maxi, res)
        #     else:
        #         res = 1
        # return maxi
        num_set = set(nums)
        num_li = list(num_set)
        num_li.sort()
        maxi = 1 
        res = 1 
        if len(nums) == 0:
            return 0
            sys.exit()
        for i in range(len(num_li)-1):
            if num_li[i]+1 == num_li[i+1]:
                maxi+=1 
                res = max(maxi, res)
            else:
                maxi = 1  
        return res