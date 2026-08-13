class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''if len(s) != len(t):
            return False

        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for ch in t:
            count[ord(ch) - ord('a')] -= 1

        return all(c == 0 for c in count)'''
        if len(s)!=len(t):
            return False
        all_alphabets = [char for char in s if char.isalpha()]
        al_alphabets = [char for char in t if char.isalpha()]
        if sorted(all_alphabets)==sorted(al_alphabets):
            return True
        else:
            return False

