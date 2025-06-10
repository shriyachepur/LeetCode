class Solution(object):
    def nearest_greater(self,nums2):
        stack=[]
        v=[]
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                v.append(stack[-1])
            else:
                v.append(-1)
            stack.append(nums2[i])
                        
        v= v[::-1]
        return v

    def nextGreaterElement(self, nums1, nums2):
        \\\
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        \\\
        out=[]
        n=self.nearest_greater(nums2)
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    out.append(n[j])
        return out

