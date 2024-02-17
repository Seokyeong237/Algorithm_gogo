class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack or (i == ")" and stack[-1] != "(") or (i == "}" and stack[-1] != "{") or (i == "]" and stack[-1] != "["):
                    return False
                stack.pop()
                    
        if len(stack) == 0:
            return True
        else:
            return False