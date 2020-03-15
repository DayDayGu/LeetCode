class Solution:

    def _per(self, current_nums, all_permution_list, current_permution_list = []):
        if len(current_nums) == 0:
            all_permution_list.append([ *current_permution_list ])
        else:
            for i in current_nums:
                new_nums = [ v for v in filter(lambda item: item != i, current_nums) ] 
                current_permution_list.append(i)
                self._per(new_nums, all_permution_list, current_permution_list)
                current_permution_list.pop()

    def permute(self, nums):
        all_permution_list = []
        self._per(nums, all_permution_list, current_permution_list = [])
        return all_permution_list

            
# test code
# s = Solution()
# print(s.permute([1, 2, 3, 4, 5, 6]))