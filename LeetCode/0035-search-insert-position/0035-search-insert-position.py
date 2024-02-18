class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        
        # mid = 1
        # 3 > 2: -> start = 0, end = 0
        # mid = 0
        # 1 < 2: -> start = 1, end = 0
        # mid = 3
        # 6 < 7: -> start = 4, end = 3
        
        while start <= end:
            mid = int((start + end) / 2)
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid
            
        return start
                
        