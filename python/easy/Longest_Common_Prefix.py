class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix_length = 0

        for chars in zip(*strs):
            if len(set(chars)) == 1:
                prefix_length += 1
            else:
                break

        return strs[0][:prefix_length]
