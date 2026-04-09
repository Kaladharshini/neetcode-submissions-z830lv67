class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
            
        string_s = defaultdict(int)
        string_t = defaultdict(int)

        for ch in s:
            string_s[ch] += 1

        for ch in t:
            string_t[ch] += 1

        return string_s == string_t



        