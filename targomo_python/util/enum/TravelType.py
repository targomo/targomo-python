from enum import Enum

class TravelType(Enum):
    CAR = "car"
    WALK = "walk"
    BIKE = "bike"
    TRANSIT = "transit"

    @classmethod
    def parse(clazz, str):

        if str is None:
            raise Exception('Travel type: "None" not supported!')

        type = getattr(clazz, str.upper(), None)
        if type is None:
            raise Exception('Travel type: "' + str + '" not supported!')

        return type