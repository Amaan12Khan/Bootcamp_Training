class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        left = 0
        count = 0
        answer = 0
        for right in range(len(s)):
            if s[right] in vowels:
                count += 1
            if right - left + 1 == k:
                answer = max(answer, count)
                if s[left] in vowels:
                    count -= 1
                left += 1
        return answer
        