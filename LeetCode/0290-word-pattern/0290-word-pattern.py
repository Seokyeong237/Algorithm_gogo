class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        map1 = []
        for i in pattern:
            map1.append(pattern.index(i))
            
        map2 = list(s.split(" "))
        
        map3 = []
        for i in map2:
            map3.append(map2.index(i))
            
        if map1 == map3:
            return True
        else:
            return False
                    
        