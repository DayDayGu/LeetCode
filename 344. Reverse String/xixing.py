class Solution:
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        str_len = len(s)
        if str_len <= 1:
            return;
        
        for i in range(0, str_len//2):
            s[i], s[str_len -1 -i] = s[str_len -1 -i], s[i]
