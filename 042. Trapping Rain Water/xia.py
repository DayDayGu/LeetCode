# class Solution:
#     def _find_buket(self, start, heights):
#         for v in range(start + 1, len(heights)):
#             if heights[start] <= heights[v]:
#                 return [start, v] 
#         return []
#     def _compute_area(self, start, end, heights):
#         min_height = min(heights[start], heights[end])
#         all_area = min_height * (end - start + 1)
#         for i in range(start, end + 1):
#             all_area -= heights[i] if heights[i] <= min_height else min_height
#         return all_area

#     # def _find_right(self, start, heights):
#     #     for 

#     #     return right

#     def trap(self, heights):
#         bukets = []    
#         i = 0
#         preview_i = 0
#         while(i < len(heights)):
#             if heights[i] != 0:
#                 buket = self._find_buket(i, heights)
#                 if len(buket) == 0:
#                     if preview_i == i:
#                         i = preview_i + 1 
#                     else:
#                         break
#                 else:
#                     bukets.append(buket)
#                     i = buket[1]
#                     preview_i = i
#             else:
#                 i += 1
#         return sum(list(map(lambda buket: self._compute_area(buket[0], buket[1], heights), bukets)))
# class Solution(object):
#     def trap(self, height):
#         """
#         没做出来
#         :type height: List[int]
#         :rtype: int
#         """
#         if len(height) < 3:
#             return 0
#         left, right = [0], []
#         max_l = 0
#         for i in range(1, len(height)):
#             max_l = max(max_l, height[i-1])
#             left.append(max_l)
#         max_r = 0
#         for j in range(len(height)-1, -1, -1):
#             if j == len(height)-1:
#                 right.append(0)
#             else:
#                 max_r = max(max_r, height[j+1])
#                 right.append(max_r)
#         right = right[::-1]
#         ans = 0
#         for i in range(len(height)):
#             curArea = (min(left[i], right[i]) - height[i])
#             if curArea > 0:
#                 ans +=curArea
#         return ans

class Solution(object):
    def trap(self, height):
        """
        更牛逼的解法
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) < 3:
            return 0
        stack, ans = [], 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                tmp = stack.pop()
                if stack:
                    w = i - 1 - stack[-1]
                    h = min(height[i], height[stack[-1]]) - height[tmp]
                    ans +=(w*h)
            stack.append(i)
        return ans
# test code 
# s = Solution()
# print(s.trap([4, 2, 3]))
