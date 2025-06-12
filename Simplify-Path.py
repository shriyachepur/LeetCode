class Solution(object):
    def simplifyPath(self, path):
        \\\
        :type path: str
        :rtype: str
        \\\
        stack=[]
        parts = path.split('/')
        for i in parts:
            if len(stack)==0 and i=='..':
                continue
            elif len(stack)!=0 and i=='..':
                    stack.pop()
            if i=='.' or i==\\:
                continue
            elif i!='..':
                stack.append(i)
            
        return '/' + '/'.join(stack)

