class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sett = set()
        for num in nums:
            sett.add(num)
        i = 1
        while i in sett:
            i+=1 
        return i
