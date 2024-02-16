class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        left = 0
        right = 0
        count = 0
        
        if s == "":
            return True
        
        while left < len(s) and right < len(t):
            if t[right] == s[left]:
                left += 1
                right += 1
                count += 1
            else:
                right += 1
        
        if count == len(s):
            return True
        else:
            return False
                
            
        