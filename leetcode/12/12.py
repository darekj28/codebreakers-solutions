class Solution:
    def intToRoman(self, num: int) -> str:
        # initialize a mapping for all possible roman characters and their values
        roman = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        # instantiate array to hold roman characters
        romanCharacters = []
        while num > 0:
            # iterate backwards to get the largest values first
            for i in reversed(range(len(values))):
                if num >= values[i]:
                    num -= values[i]
                    romanCharacters.append(roman[i])
                    break
        return "".join(romanCharacters)