from targomo_python.util.Util import Util
from targomo_python.util.enum.EdgeWeightType import EdgeWeightType
from targomo_python.util.enum.PathSerializerType import PathSerializerType
from targomo_python.util.enum.PolygonIntersectionMode import PolygonIntersectionMode
from targomo_python.util.enum.PolygonSerializationType import PolygonSerializationType

class TravelOptions:
    'This class represents the configuration for one request'

    def __init__(self):
        self.sources = []
        self.targets = []
        self.travelTimes = []
        self.travelType = None
        self.buffer = None
        self.simplifyMeter = None
        self.quadrantSegments = None
        self.srid = None
        self.travelDate = Util.currentDate()
        self.travelTime = Util.currentTime()
        self.minPolygonHoleSize = 100000000
        self.intersectionMode = PolygonIntersectionMode.UNION
        self.polygonSerializationType = PolygonSerializationType.JSON
        self.pathSerializer = PathSerializerType.COMPACT_PATH_SERIALIZER
        self.edgeWeightType = EdgeWeightType.TIME
        self.maxEdgeWeight = None
        self.frameDuration = None
        self.reverse = None
        self.bikeSpeed = None
        self.bikeUphill = None
        self.bikeDownhill = None
        self.walkSpeed = None
        self.walkUphill = None
        self.walkDownhill = None
        self.disableCache = None
        self.statisticGroupId = None
        self.recommendations = None
        self.elevation = None
        self.rushHour = None

    def setPolygonSerializationType(self, polygonSerializationType):
        self.polygonSerializationType = polygonSerializationType

    def getPolygonSerializationType(self):
        return self.polygonSerializationType

    def setServiceUrl(self, serviceUrl):
        self.serviceUrl = serviceUrl

    def getServiceUrl(self):
        return self.serviceUrl

    def setServiceKey(self, serviceKey):
        self.serviceKey = serviceKey

    def getServiceKey(self):
        return self.serviceKey

    def setSources(self, sources):
        self.sources = sources

    def getSources(self):
        return self.sources

    def addSource(self, source):
        self.sources.append(source)

    def setTargets(self, targets):
        self.targets = targets

    def getTargets(self):
        return self.targets

    def addTarget(self, target):
        self.targets.append(target)

    def setTravelTimes(self, travelTimes):
        self.travelTimes = travelTimes

    def getTravelTimes(self):
        return self.travelTimes

    def addTravelTime(self, travelTime):
        self.travelTimes.append(travelTime)

    def setMinPolygonHoleSize(self, minPolygonHoleSize):
        self.minPolygonHoleSize = minPolygonHoleSize

    def getMinPolygonHoleSize(self):
        return self.minPolygonHoleSize

    def setTravelType(self, travelType):
        self.travelType = travelType

    def getTravelType(self):
        return self.travelType

    def setTravelTime(self, travelTime):
        self.travelTime = travelTime

    def getTravelTime(self):
        return self.travelTime

    def setTravelDate(self, travelDate):
        self.travelDate = travelDate

    def getTravelDate(self):
        return self.travelDate

    def setPolygonIntersectionMode(self, intersectionMode):
        self.intersectionMode = intersectionMode

    def getPolygonIntersectionMode(self):
        return self.intersectionMode

    def setBuffer(self, buffer):
        self.buffer = buffer

    def getBuffer(self):
        return self.buffer

    def setSimplifyMeter(self, simplifyMeter):
        self.simplifyMeter = simplifyMeter

    def getSimplifyMeter(self):
        return self.simplifyMeter

    def setQuadrantSegments(self, quadrantSegments):
        self.quadrantSegments = quadrantSegments

    def getQuadrantSegments(self):
        return self.quadrantSegments

    def setSrid(self, srid):
        self.srid = srid

    def getSrid(self):
        return self.srid

    def setPathSerializer(self, path_serializer):
        self.pathSerializer = path_serializer

    def getPathSerializer(self):
        return self.pathSerializer

    def getEdgeWeightType(self):
        return self.edgeWeightType

    def setEdgeWeightType(self, edge_weight_type):
        self.edgeWeightType = edge_weight_type

    def getMaxEdgeWeight(self):
        return self.maxEdgeWeight

    def setMaxEdgeWeight(self, max_edge_weight):
        self.maxEdgeWeight = max_edge_weight

    def getFrameDuration(self):
        return self.frameDuration

    def setFrameDuration(self, frame_duration):
        self.frameDuration = frame_duration

    def getReverse(self):
        return self.reverse

    def setReverse(self, reverse):
        self.reverse = reverse

    def getBikeSpeed(self):
        return self.bikeSpeed

    def setBikeSpeed(self, bike_speed):
        self.bikeSpeed = bike_speed

    def getBikeUphill(self):
        return self.bikeUphill

    def setBikeUphill(self, bike_uphill):
        self.bikeUphill = bike_uphill

    def getBikeDownhill(self):
        return self.bikeDownhill

    def setBikeDownhill(self, bike_downhill):
        self.bikeDownhill = bike_downhill

    def getWalkSpeed(self):
        return self.walkSpeed

    def setWalkSpeed(self, walk_speed):
        self.walkSpeed = walk_speed

    def getWalkUphill(self):
        return self.walkUphill

    def setWalkUphill(self, walk_uphill):
        self.walkUphill = walk_uphill

    def getWalkDownhill(self):
        return self.walkDownhill

    def setWalkDownhill(self, walk_downhill):
        self.walkDownhill = walk_downhill

    def getDisableCache(self):
        return self.disableCache

    def setDisableCache(self, disable_cache):
        self.disableCache = disable_cache

    def getStatisticGroupId(self):
        return self.statisticGroupId

    def setStatisticGroupId(self, statistic_group_id):
        self.statisticGroupId = statistic_group_id

    def getRecommendations(self):
        return self.recommendations

    def setRecommendations(self, recommendations):
        self.recommendations = recommendations

    def getElevation(self):
        return self.elevation

    def setElevation(self, elevation):
        self.elevation = elevation

    def getRushHour(self):
        return self.rushHour

    def setRushHour(self, rushHour):
        self.rushHour = rushHour
