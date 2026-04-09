class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        string_s = defaultdict(int)
        string_t = defaultdict(int)

        for c in s:
            string_s[c] += 1
        
        for c in t:
            string_t[c] += 1

        return string_s == string_t

      