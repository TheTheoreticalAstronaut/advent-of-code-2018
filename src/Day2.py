from AOCChallenge import AOCChallenge
from Types import Input
from string import ascii_lowercase
from operator import or_, truth


class Day2(AOCChallenge):
    INPUT_FILENAME = "resources/day2_input.dat"

    # Public
    def __init__(self):
        super().__init__(Day2.INPUT_FILENAME, Input.STR_PER_LINE)

    def run_part_one(self) -> int:
        letter_repeated_twice = [False] * len(self._input)
        letter_repeated_thrice = [False] * len(self._input)
        for c in ascii_lowercase:
            c_counts = [str_in.count(c) for str_in in self._input]
            letter_repeated_twice = list(map(or_, letter_repeated_twice, [count == 2 for count in c_counts]))
            letter_repeated_thrice = list(map(or_, letter_repeated_thrice, [count == 3 for count in c_counts]))
        return sum(map(truth, letter_repeated_twice))*sum(map(truth, letter_repeated_thrice))

    def run_part_two(self) -> str:
        for i in range(len(self._input[0])):
            input_letter_removed = [str_in[:i]+str_in[i+1:] for str_in in self._input]
            letter_removed_set = set()
            for str_in in input_letter_removed:
                if str_in in letter_removed_set:
                    return str_in
                else:
                    letter_removed_set.add(str_in)
