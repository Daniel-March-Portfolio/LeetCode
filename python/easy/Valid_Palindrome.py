class Solution:
    ignore_chars = set("""!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c""")

    def isPalindrome(self, s: str) -> bool:
        left_idx = self.next_letter_idx(s, -1)
        right_idx = self.prev_letter_idx(s, len(s))
        while left_idx < right_idx:
            if s[left_idx].lower() != s[right_idx].lower():
                return False
            left_idx = self.next_letter_idx(s, left_idx)
            right_idx = self.prev_letter_idx(s, right_idx)
        return True

    def prev_letter_idx(self, s: str, cur_idx: int) -> int:
        while cur_idx > 0:
            cur_idx -= 1
            if s[cur_idx] not in self.ignore_chars:
                break
        return cur_idx

    def next_letter_idx(self, s: str, cur_idx: int) -> int:
        while cur_idx < len(s)-1:
            cur_idx += 1
            if s[cur_idx] not in self.ignore_chars:
                break
        return cur_idx