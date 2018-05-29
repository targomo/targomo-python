from enum import Enum


class EdgeWeightType(Enum):
    DISTANCE = "distance"
    TIME = "time"

    @classmethod
    def parse(cls, str_to_parse):
        return getattr(cls, str_to_parse.upper(), None)
