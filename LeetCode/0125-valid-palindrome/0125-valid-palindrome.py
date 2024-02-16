class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'\W+|_', '', s).lower()
        reverse_s = s[::-1]
        
        start = 0
        
        while start < len(s):
            if s[start] == reverse_s[start]:
                start += 1
            else:
                return False
            
        return True
        