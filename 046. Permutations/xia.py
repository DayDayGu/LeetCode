class Solution:
    def permute(self, nums):
        list_length = len(nums)
        if list_length == 1:
            return [ nums ]
        indics = [ i for i in range(list_length) ] 
        permute_result = [] 
        for step in range(list_length):
            pre_index = 0
            while(pre_index < list_length - 1):
                permute_result.append(
                    [ nums[i] for i in indics ] 
                )
                indics[pre_index], indics[pre_index + 1] = indics[pre_index + 1], indics[pre_index]
                pre_index += 1
        return permute_result
             
s = Solution()

print(len(s.permute([5, 4, 6, 2])))