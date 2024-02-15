class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """        
        s_list = list(s)
        sum = 0
        start = 0
        end = 1
        
        while end <= len(s_list):
            if start == len(s_list)-1:
                if s_list[start] == "I":
                    sum += 1
                elif s_list[start] == "V":
                    sum += 5
                elif s_list[start] == "X":
                    sum += 10
                elif s_list[start] == "L":
                    sum += 50
                elif s_list[start] == "C":
                    sum += 100
                elif s_list[start] == "D":
                    sum += 500
                elif s_list[start] == "M":
                    sum += 1000
                break
            if s_list[start]=="I" and s_list[end]=="V":
                sum += 4
                start += 1
                end += 1 
            elif s_list[start]=="I" and s_list[end]=="X":
                sum += 9
                start += 1
                end += 1 
            elif s_list[start]=="I" and (s_list[end]!="V" or s_list[end]!="X"):
                sum += 1
            elif s_list[start]=="X" and s_list[end]=="L":
                sum += 40
                start += 1
                end += 1 
            elif s_list[start]=="X" and s_list[end]=="C":
                sum += 90
                start += 1
                end += 1 
            elif s_list[start]=="X" and (s_list[end]!="L" or s_list[end]!="C"):
                sum += 10
            elif s_list[start]=="C" and s_list[end]=="D":
                sum += 400
                start += 1
                end += 1 
            elif s_list[start]=="C" and s_list[end]=="M":
                sum += 900
                start += 1
                end += 1 
            elif s_list[start]=="C" and (s_list[end]!="D" or s_list[end]!="M"):
                sum += 100
            elif s_list[start] == "V":
                sum += 5
            elif s_list[start] == "L":
                sum += 50
            elif s_list[start] == "D":
                sum += 500
            elif s_list[start] == "M":
                sum += 1000
            start += 1
            end += 1     
                    
        return sum
        
        