class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}

        for s_letter in s:
            if s_letter not in counter:
                counter[s_letter] = 0
            counter[s_letter] += 1

        for t_letter in t:
            if t_letter not in counter:
                counter[t_letter] = 0
            counter[t_letter] -= 1

        return set(counter.values()) == {0}