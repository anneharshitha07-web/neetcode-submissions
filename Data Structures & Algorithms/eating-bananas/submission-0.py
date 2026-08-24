class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right
        
        while left <= right:
            mid = (left + right) // 2
            total_hours = 0
            for pile in piles:
                total_hours += (pile + mid - 1) // mid 
            if total_hours <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return result
    