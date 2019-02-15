class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        input_len = len(nums)
        if input_len <= 1:
            return
        left = 0
        right = 1
        while right < len(nums):
            if nums[left] == 0 and nums[right] != 0:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp
                left += 1
            elif nums[left] != 0:
                left += 1
            right += 1
