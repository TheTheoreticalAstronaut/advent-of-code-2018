from enum import Enum
from typing import List,Tuple

ListInt = List[int]
TupleStr = Tuple[str]


class Input(Enum):
    UNDEFINED = 0
    INT_PER_LINE = 1
    STR_PER_LINE = 2
    SPACE_SEPARATED_INT = 3
    REGEX_PER_LINE = 4


class Challenge(Enum):
    UNDEFINED = 0
    DAY_1 = 1
    DAY_2 = 2
    DAY_3 = 3
    DAY_8 = 8
