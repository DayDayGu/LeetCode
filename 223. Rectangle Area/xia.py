class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        left_line = max(A, E)
        right_line = min(C, G)
        top_line = min(D, H)
        bottom_line = max(B, F)

        if (left_line > right_line) or (bottom_line > top_line):
            inner_area = 0
        else:
            inner_area = (left_line - right_line) * (top_line - bottom_line)

        sum_area = (G - E) * (H -F) + (C - A) * (D - B) 

        return sum_area - inner_area