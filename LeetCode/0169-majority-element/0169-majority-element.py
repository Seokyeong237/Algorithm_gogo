class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        nums_set = set(nums)
        
        for i in list(nums_set):
            dic[i] = nums.count(i)
            
        answer = max(dic,key=dic.get)
        return int(answer)
            
        