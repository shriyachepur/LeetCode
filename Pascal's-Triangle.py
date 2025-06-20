class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal=[]
        for r in range(numRows):
            x = [1] * (r + 1)
            for i in range(1, r):
                x[i] = pascal[r-1][i-1] + pascal[r-1][i]
            pascal.append(x)

        return pascal

        