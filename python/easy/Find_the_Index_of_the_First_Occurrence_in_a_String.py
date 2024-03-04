class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_haystack = len(haystack)
        len_needle = len(needle)

        for idx in range(len_haystack - len_needle + 1):
            if self._is_index_in_the_start_of_occurrence(idx, haystack, needle):
                return idx

        return -1

    def _is_index_in_the_start_of_occurrence(self, idx: int, haystack: str, needle: str) -> bool:
        for idx_in_needle, char in enumerate(needle):
            if char != haystack[idx_in_needle + idx]:
                return False
        return True