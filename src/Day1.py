from AOCChallenge import AOCChallenge
from Types import Input


class Day1(AOCChallenge):
    INPUT_FILENAME = "resources/day1_input.dat"

    # Public
    def __init__(self):
        super().__init__(Day1.INPUT_FILENAME, Input.INT_PER_LINE)

    def run_part_one(self) -> int:
        return sum(self._input)

    def run_part_two(self) -> int:
        current_frequency = 0
        frequency_set = set()
        while True:
            for frequency in self._input:
                current_frequency += frequency
                if current_frequency in frequency_set:
                    return current_frequency
                else:
                    frequency_set.add(current_frequency)
