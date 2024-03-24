from string import ascii_lowercase

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        accordance_s = {}
        accordance_t = {}

        for s_letter, t_letter in zip(s, t):
            if s_letter in accordance_s and accordance_s[s_letter] != t_letter:
                return False
            if t_letter in accordance_t and accordance_t[t_letter] != s_letter:
                return False
            accordance_s[s_letter] = t_letter
            accordance_t[t_letter] = s_letter

        return True