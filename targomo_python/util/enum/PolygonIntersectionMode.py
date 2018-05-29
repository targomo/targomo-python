from enum import Enum

class PolygonIntersectionMode(Enum):
    UNION = "union"
    INTERSECTION = "intersection"
    AVERAGE = "average"

    @classmethod
    def parse(clazz, str):
        
        if str is None:
            raise Exception('PolygonIntersectionMode: "None" not supported!')

        type = getattr(clazz, str.upper(), None)
        if type is None:
            raise Exception('PolygonIntersectionMode: "' + str + '" not supported!')

        return type