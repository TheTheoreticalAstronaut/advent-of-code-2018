from Types import Input
import re


class AOCChallenge:
    def __init__(self, input_filename: str, input_type: Input, additional_input_info=""):
        self._input_filename = input_filename
        self._read_input(input_type, additional_input_info)

    def run_part_one(self) -> int:
        pass

    def run_part_two(self) -> int:
        pass

    def _read_per_line_int_input(self) -> None:
        with open(self._input_filename, "r") as file:
            self._input = [int(line.rstrip()) for line in file]

    def _read_per_line_str_input(self) -> None:
        with open(self._input_filename, "r") as file:
            self._input = [line.rstrip() for line in file]

    def _read_space_separated_int_input(self) -> None:
        with open(self._input_filename, "r") as file:
            self._input = [int(x) for x in file.read().split()]

    def _read_per_line_regex_input(self, regex_expression: str):
        compiled_regex = re.compile(regex_expression)
        with open(self._input_filename, "r") as file:
            self._input = [match for line in file for match in re.findall(compiled_regex, line)]

    def _read_input(self, input_type: Input, additional_input_info="") -> None:
        if input_type == Input.UNDEFINED:
            return
        elif input_type == Input.INT_PER_LINE:
            return self._read_per_line_int_input()
        elif input_type == Input.STR_PER_LINE:
            return self._read_per_line_str_input()
        elif input_type == Input.SPACE_SEPARATED_INT:
            return self._read_space_separated_int_input()
        elif input_type == Input.REGEX_PER_LINE:
            return self._read_per_line_regex_input(additional_input_info)
        return
