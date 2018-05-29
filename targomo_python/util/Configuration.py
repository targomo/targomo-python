class Configuration:
    'This class represents a single configuration, build from traveloptions, for a request'

    @staticmethod
    def build(travelOptions):
        sources = travelOptions.getSources()

        for source in sources:
            source['tm'] = {}
            if 'travelType' in source.keys() and not source['travelType'] is None:
                travelType = source['travelType']
            else:
                travelType = travelOptions.getTravelType().value

            source['tm'][travelType] = {}
            if travelType == 'transit' or travelType == 'biketransit':
                source['tm'][travelType]['frame'] = {}
                source['tm'][travelType]['frame']['time'] = travelOptions.getTravelTime()
                source['tm'][travelType]['frame']['date'] = travelOptions.getTravelDate()
                if not travelOptions.getFrameDuration() is None:
                    source['tm'][travelType]['frame']['duration'] = travelOptions.getFrameDuration()
                if not travelOptions.getRecommendations() is None:
                    source['tm'][travelType]['recommendations'] = travelOptions.getRecommendations()

            if travelType == 'bike':
                # bike specific
                if not travelOptions.getBikeSpeed() is None:
                    source['tm'][travelType]['speed'] = travelOptions.getBikeSpeed()
                if not travelOptions.getBikeUphill() is None:
                    source['tm'][travelType]['uphill'] = travelOptions.getBikeUphill()
                if not travelOptions.getBikeDownhill() is None:
                    source['tm'][travelType]['downhill'] = travelOptions.getBikeDownhill()

            if travelType == 'walk':
                #  walk specific
                if not travelOptions.getWalkSpeed() is None:
                    source['tm'][travelType]['speed'] = travelOptions.getWalkSpeed()
                if not travelOptions.getWalkUphill() is None:
                    source['tm'][travelType]['uphill'] = travelOptions.getWalkUphill()
                if not travelOptions.getWalkDownhill() is None:
                    source['tm'][travelType]['downhill'] = travelOptions.getWalkDownhill()

            if travelType == 'car':
                #  car specific
                if not travelOptions.getRushHour() is None:
                    source['tm'][travelType]['rushHour'] = travelOptions.getRushHour()

        cfg = {
            "sources": sources
        }

        if travelOptions.getTravelTimes():
            polygonJson = {
                "values": travelOptions.getTravelTimes(),
                "intersectionMode": travelOptions.getPolygonIntersectionMode().value,
                "serializer": travelOptions.getPolygonSerializationType().value,
                "pointReduction": True,
                "minPolygonHoleSize": travelOptions.getMinPolygonHoleSize()
            }

            if not travelOptions.getBuffer() is None:
                polygonJson['buffer'] = travelOptions.getBuffer()
            if not travelOptions.getSimplifyMeter() is None:
                polygonJson['simplify'] = travelOptions.getSimplifyMeter()
            if not travelOptions.getSrid() is None:
                polygonJson['srid'] = travelOptions.getSrid()
            if not travelOptions.getQuadrantSegments() is None:
                polygonJson['quadrantSegments'] = travelOptions.getQuadrantSegments()

            cfg['polygon'] = polygonJson

        if not travelOptions.getPathSerializer() is None:
            cfg['pathSerializer'] = travelOptions.getPathSerializer().value

        if travelOptions.getTargets():
            cfg['targets'] = travelOptions.getTargets()

        if not travelOptions.getEdgeWeightType() is None:
            cfg['edgeWeightType'] = travelOptions.getEdgeWeightType().value

        if not travelOptions.getMaxEdgeWeight() is None:
            cfg['maxEdgeWeight'] = travelOptions.getMaxEdgeWeight()

        if not travelOptions.getReverse() is None:
            cfg['reverse'] = travelOptions.getReverse()

        if not travelOptions.getDisableCache() is None:
            cfg['disableCache'] = travelOptions.getDisableCache()

        if not travelOptions.getStatisticGroupId() is None:
            cfg['statisticGroupId'] = travelOptions.getStatisticGroupId()

        if not travelOptions.getElevation() is None:
            cfg['elevation'] = travelOptions.getElevation()

        return cfg
