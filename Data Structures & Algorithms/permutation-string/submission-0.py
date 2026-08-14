class Solution:
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False
            
        # Initialize frequency arrays for 26 lowercase English letters
        s1_counts = [0] * 26
        s2_counts = [0] * 26
        
        # Count frequencies for the initial window
        for i in range(len1):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1
            
        # If the initial window matches, a permutation is found
        if s1_counts == s2_counts:
            return True
            
        # Slide the window across s2
        for i in range(len1, len2):
            # Add the new character entering the window
            s2_counts[ord(s2[i]) - ord('a')] += 1
            # Remove the old character leaving the window
            s2_counts[ord(s2[i - len1]) - ord('a')] -= 1
            
            # Check if current window matches s1's frequency
            if s1_counts == s2_counts:
                return True
                
        return False
    