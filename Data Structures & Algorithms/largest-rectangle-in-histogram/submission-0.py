class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        stack = [] # Stores pairs: (index, height)
        
        for i, h in enumerate(heights):
            start = i
            # Pop elements from stack if current height is shorter
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                # Area = height * (current_index - original_start_index)
                max_area = max(max_area, height * (i - idx))
                start = idx # Current bar can extend back to the popped bar's start
                
            stack.append((start, h))
            
        # Clear remaining elements in the stack
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
            
        return max_area
    