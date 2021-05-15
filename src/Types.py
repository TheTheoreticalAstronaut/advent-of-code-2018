from enum import Enum
from typing import List

ListInt = List[int]


class Input(Enum):
    UNDEFINED = 0
    INT_PER_LINE = 1
    SPACE_SEPARATED_INT = 2


class Challenge(Enum):
    UNDEFINED = 0
    DAY_1 = 1
    DAY_8 = 8
