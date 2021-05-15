from enum import Enum
from typing import List

ListInt = List[int]


class Input(Enum):
    UNDEFINED = 0
    INT_PER_LINE = 1
    STR_PER_LINE = 2
    SPACE_SEPARATED_INT = 3


class Challenge(Enum):
    UNDEFINED = 0
    DAY_1 = 1
    DAY_2 = 2
    DAY_8 = 8
