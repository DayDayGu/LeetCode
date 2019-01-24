class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list_len = len(nums)
        # init result list
        result = [1 for i in range(list_len)]
        factor = 1
        for i in range(list_len):
            result[i] *= factor
            factor *= nums[i]
        
        # reset factor
        factor = 1
        for i in reversed(range(list_len)):
            result[i] *= factor
            factor *= nums[i]
        
        return result
