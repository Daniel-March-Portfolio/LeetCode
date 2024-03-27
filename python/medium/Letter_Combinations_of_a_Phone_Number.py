class Solution:
    translator = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz",
    }
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        combinations = self.getCombinations(int(digits))
        return ["".join(combination) for combination in combinations]

    def getCombinations(self, number: int) -> List[List[str]]:
        if number < 2:
            return []
        letters = self.translator[number%10]
        next_combinations = self.getCombinations(number//10)
        if len(next_combinations) == 0:
            return list(map(list, list(letters)))
        combinations = []
        for letter in letters:
            for combination in next_combinations:
                combinations.append(combination + [letter])
        return combinations