class Solution:
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """

        len_str = len(s)         

        i = 0

        while ( i < len_str // 2 ):
            swap_index = len_str - i - 1
            s[i], s[swap_index] = s[swap_index], s[i]
            i += 1
