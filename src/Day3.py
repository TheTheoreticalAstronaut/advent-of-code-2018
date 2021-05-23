from AOCChallenge import AOCChallenge
from Types import Input,TupleStr,ListInt


class Patch:
    def __init__(self, data_tuple: TupleStr):
        if len(data_tuple) != 5:
            print("Unexpected data_tuple size: " + len(data_tuple))
            return
        self._id = int(data_tuple[0])
        self._left_shift = int(data_tuple[1])
        self._top_shift = int(data_tuple[2])
        self._width = int(data_tuple[3])
        self._height = int(data_tuple[4])
        self._overlaps = False

    @property
    def id(self) -> int:
        return self._id

    @property
    def min_h(self) -> int:
        return self._left_shift

    @property
    def max_h(self) -> int:
        return self._left_shift+self._width-1

    @property
    def min_v(self) -> int:
        return self._top_shift

    @property
    def max_v(self) -> int:
        return self._top_shift+self._height-1

    @property
    def overlaps(self) -> bool:
        return self._overlaps

    def set_overlap(self, value=True) -> None:
        self._overlaps = value

    @staticmethod
    def find_overlap(patch_0, patch_1):
        if patch_0.min_h > patch_1.max_h or patch_0.max_h < patch_1.min_h:
            return []
        if patch_0.min_v > patch_1.max_v or patch_0.max_v < patch_1.min_v:
            return []

        patch_0.set_overlap()
        patch_1.set_overlap()

        min_h_overlap = max(patch_0.min_h, patch_1.min_h)
        max_h_overlap = min(patch_0.max_h, patch_1.max_h)
        min_v_overlap = max(patch_0.min_v, patch_1.min_v)
        max_v_overlap = min(patch_0.max_v, patch_1.max_v)
        return [(h, v) for h in range(min_h_overlap, max_h_overlap+1) for v in range(min_v_overlap, max_v_overlap+1)]


class Day3(AOCChallenge):
    INPUT_FILENAME = "resources/day3_input.dat"
    INPUT_REGEX = "\#([0-9]+)\s@\s([0-9]+),([0-9]+):\s([0-9]+)x([0-9]+)"

    # Public
    def __init__(self):
        super().__init__(Day3.INPUT_FILENAME, Input.REGEX_PER_LINE, Day3.INPUT_REGEX)
        self._patches = [Patch(input_data) for input_data in self._input]
        self._overlapping_squares = self._find_overlaps()

    def run_part_one(self) -> int:
        return len(self._overlapping_squares)

    def run_part_two(self) -> int:
        return next(patch.id for patch in self._patches if not patch.overlaps)

    def _find_overlaps(self):
        overlaps = []
        for i in range(len(self._patches)):
            for j in range(i+1, len(self._patches)):
                patch_overlap = Patch.find_overlap(self._patches[i], self._patches[j])
                if patch_overlap:
                    overlaps += patch_overlap
        return set(overlaps)
