class Solution(object):
    def singleNumber(self, nums):
        """
            o(n)
        """
        a = 0
        for i in nums:
            a ^= i
        return a