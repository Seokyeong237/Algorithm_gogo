class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        dic = {}
        dic1 = {}
        count = 1
        for i in range(len(ransomNote)):
            key = ransomNote[i]
            if key in dic:
                dic[key] = dic.get(key) + 1
            else:
                dic[key] = count
           
        count = 1
        for i in range(len(magazine)):
            key = magazine[i]
            if key in dic1:
                dic1[key] = dic1.get(key) + 1
            else:
                dic1[key] = count
            
        print(dic)
        print(dic1)
            
        for i in ransomNote:
            if dic.get(i) > dic1.get(i):
                return False
            
        return True
                