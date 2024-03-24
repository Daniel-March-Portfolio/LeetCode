class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used_list = []
        longest = 0

        for letter in s:
            if letter not in used_list:
                used_list.append(letter)
            else:
                longest = max(longest, len(used_list))
                used_list = used_list[used_list.index(letter)+1:] + [letter]

        longest = max(longest, len(used_list))
        return longest