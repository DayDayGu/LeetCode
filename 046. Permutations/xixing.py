class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]
        
        tmp_result = []
        for item in nums:
            for inner_res in self.permute([i for i in nums if i != item]):
                tmp_result.append([item] + inner_res)
        return tmp_result
