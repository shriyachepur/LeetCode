class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        pascal=[]
        for r in range(rowIndex+1):
            x = [1] * (r + 1)
            for i in range(1, r):
                x[i] = pascal[r-1][i-1] + pascal[r-1][i]
            pascal.append(x)

        return pascal[rowIndex]