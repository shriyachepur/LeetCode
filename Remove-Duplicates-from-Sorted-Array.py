class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow=0
        fast=1
        while fast<len(nums)-1:
            if nums[slow]==nums[fast]:
                fast=fast+1
            if nums[slow]!=nums[fast]:
                nums[slow+1]=nums[fast]
                slow=slow+1
                #fast=fast+1
        unique=set(nums)
        return len(unique)
            

        