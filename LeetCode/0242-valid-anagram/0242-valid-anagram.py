class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        map = {}
        map1 = {}
        count = 1
        
        for i in range(len(s)):
            key = s[i]
            if key in map:
                map[key] = map.get(key) + 1
            else:
                map[key] = count
        
        for i in range(len(t)):
            key = t[i]
            if key in map1:
                map1[key] = map1.get(key) + 1
            else:
                map1[key] = count
            
        if (map.keys() == map1.keys() and map.values() == map1.values()):
            return True
        else:
            return False
        