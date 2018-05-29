from enum import Enum


class PathSerializerType(Enum):
    COMPACT_PATH_SERIALIZER = "compact"
    GEO_JSON_PATH_SERIALIZER = "geojson"

    @classmethod
    def parse(cls, str):
        return getattr(cls, str.upper(), None)
