class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end_of_word_i = len(s) - 1
        start_of_word_i = len(s) - 1

        while start_of_word_i >= 0:
            if s[start_of_word_i] == " ":
                if start_of_word_i == end_of_word_i:
                    start_of_word_i -= 1
                    end_of_word_i -= 1
                else:
                    break
            else:
                start_of_word_i -= 1

        return end_of_word_i - start_of_word_i
