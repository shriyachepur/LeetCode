class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1=[]
        t1=[]
        for i in s:
            if i!='#':
                s1.append(i)
            if i=='#' and len(s1)!=0:
                s1.pop()
        for i in t:
            if i!='#':
                t1.append(i)
            if i=='#'and len(t1)!=0:
                t1.pop()
        return s1==t1
        
        