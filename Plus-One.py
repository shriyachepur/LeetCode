class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=0
        for i in digits:
            num=(num*10)+i
        num=num+1
        x=[int(d) for d in str(num)]
        return x

        