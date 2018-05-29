from enum import Enum

class PolygonSerializationType(Enum):
    JSON = "json"
    GEOJSON = "geojson"

    @classmethod
    def parse(clazz, str):
      return getattr(clazz, str.upper(), None)