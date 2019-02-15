class Solution:
    # Time Limit Exceeded
    # O(n2) time complex
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 1:
            return 0

        max_height = max(height)
        result = 0

        for i in range(1, max_height + 1):
            last_pos = None
            for pos in range(0, len(height)):
                if height[pos] >= i and last_pos is not None:
                    result += pos - last_pos - 1
                    last_pos = pos
                elif height[pos] >= i:
                    last_pos = pos

        return result
