class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def find(arr,val,low,high):
            if low>high:
                return low
            mid=(low+high)//2
            if arr[mid]==val:
                return mid
            elif val < arr[mid]:
                return find(arr, val, low, mid - 1)
            else:
                return find(arr,val,mid+1,high)
        return find(nums, target, 0, len(nums) - 1)
            
        