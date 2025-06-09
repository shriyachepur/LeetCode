class Solution(object):
    def isValid(self, s):
        \\\
        :type s: str
        :rtype: bool
        \\\
        parenthesis = {'(':')','{':'}','[':']'}
        stack = []
        for i in range(len(s)):
            if s[i] in \({[\:
                stack.append(parenthesis[s[i]])
            if s[i] in \)}]\:
                if len(stack)==0:
                    return False
                if s[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False

        
        