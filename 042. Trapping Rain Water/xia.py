class Solution:
    def _find_buket(self, start, heights):
        for v in range(start + 1, len(heights)):
            if heights[start] <= heights[v]:
                return [start, v] 
        return []
    def _compute_area(self, start, end, heights):
        min_height = min(heights[start], heights[end])
        all_area = min_height * (end - start + 1)
        for i in range(start, end + 1):
            all_area -= heights[i] if heights[i] <= min_height else min_height
        return all_area

    # def _find_right(self, start, heights):
    #     for 

    #     return right

    def trap(self, heights):
        bukets = []    
        i = 0
        preview_i = 0
        while(i < len(heights)):
            if heights[i] != 0:
                buket = self._find_buket(i, heights)
                if len(buket) == 0:
                    if preview_i == i:
                        i = preview_i + 1 
                    else:
                        break
                else:
                    bukets.append(buket)
                    i = buket[1]
                    preview_i = i
            else:
                i += 1
        return sum(list(map(lambda buket: self._compute_area(buket[0], buket[1], heights), bukets)))

# test code 
# s = Solution()
# print(s.trap([4, 2, 3]))
