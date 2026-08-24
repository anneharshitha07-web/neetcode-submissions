class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output = []
        q = deque() 
        
        for i, val in enumerate(nums):
            
            if q and q[0] < i - k + 1:
                q.popleft()
            while q and nums[q[-1]] < val:
                q.pop()
            q.append(i)
            
            if i >= k - 1:
                output.append(nums[q[0]])
                
        return output
    