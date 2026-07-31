
class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> list[str]:
        """Decodes a single string back to a list of strings."""
        decoded_strs = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            
            
            start = j + 1
            end = start + length
            
            decoded_strs.append(s[start:end])
            
            i = end
            
        return decoded_strs
