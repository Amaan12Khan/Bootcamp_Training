class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        # Sort the strings alphabetically
        strs.sort()
        
        # Get the first and last strings in the sorted list
        first = strs[0]
        last = strs[-1]
        
        result = []
        
        # Compare characters of the first and last string
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            result.append(first[i])
            
        # Join the matching characters back into a single string
        return "".join(result)