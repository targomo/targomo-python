import json
import argparse
import logging
from targomo_python.util.TravelOptions import TravelOptions
from targomo_python.util.enum.PolygonSerializationType import PolygonSerializationType
from targomo_python.util.enum.TravelType import TravelType
from targomo_python.util.enum.EdgeWeightType import EdgeWeightType
from targomo_python.rest.ServiceExecutor import ServiceExecutor

def source(arg):
    # For simplity, assume arg is a pair of integers
    # separated by a comma. If you want to do more
    # validation, raise argparse.ArgumentError if you
    # encounter a problem.
    return [float(x) for x in arg.split(';')]

def createParser():
    parser = argparse.ArgumentParser(prog="python -m targomo_python.cli", description="Query the Targomo Polygon service using python", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--time",              type=int,    help="The time in seconds of the day: 1.30 p.m. = 13 * 3600 + 30 * 60 = 48600 (transit only)", default=43200)
    parser.add_argument("--date",              type=int,    help="The date in the format YYYYMMDD, e.g.: 20160727 for the 27th of July 2016 (transit only)", default=20162707)
    parser.add_argument("--polygonSerializer", type=str,    help="The serializer for the polygons: json or geojson", default="geojson")
    parser.add_argument("--edgeWeightType",    type=str,    help="The method by which we measure reach: time or distance", default="time")
    parser.add_argument("--buffer",            type=float,  help="The buffer (in srid units) that should be generated around the polygons.", default=None)
    parser.add_argument("--minHoleSize",       type=int,    help="The area threshold of a hole inside a polygon (in meters squared).", default=None)
    parser.add_argument("--simplify",          type=int,    help="The threshold (in meter) that should be used for Douglas-Puecker (before buffering, max 500m).", default=None)
    parser.add_argument("--srid",              type=int,    help="The target SRID (Spatial Reference System Identifier), all that are supported via PostGIS.", default=None)
    parser.add_argument("--quadrantSegments",  type=int,    help="The number of quadrant segements (max 8), see: http://postgis.net/docs/ST_Buffer.html.", default=None)
    parser.add_argument("--frameDuration",     type=int,    help="The window (in seconds) during which connections are identified.", default=None)
    parser.add_argument("--reverse",           type=bool,   help="Whether or not to measure from sources (default) or towards sources.", default=None)
    parser.add_argument("--bikeSpeed",         type=float,  help="Bike speed km/h (travelType 'bike' only).", default=None)
    parser.add_argument("--bikeUphill",        type=float,  help="Penalty applied to uphill bike travel.", default=None)
    parser.add_argument("--bikeDownhill",      type=float,  help="Penalty applied to downhill bike travel.", default=None)
    parser.add_argument("--walkSpeed",         type=float,  help="Walk speed km/h (travelType 'walk' only).", default=None)
    parser.add_argument("--walkUphill",        type=float,  help="Penalty applied to uphill walk travel.", default=None)
    parser.add_argument("--walkDownhill",      type=float,  help="Penalty applied to downhill bike travel.", default=None)

    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument("--travelTimes",       type=int,    help="The travel time in seconds as a list of integers.", nargs="+", required=True)
    requiredNamed.add_argument("--serviceUrl",        type=str,    help="The URL of the Targomo API endpoint.", required=True)
    requiredNamed.add_argument("--serviceKey",        type=str,    help="Your personal key for the API.", required=True)
    requiredNamed.add_argument("--travelType",        type=str,    help="The travel type for the request: car, walk, bike or transit", required=True)
    requiredNamed.add_argument("--source",            type=source, help="The source as doubles (lat,lng) separated by ';'.", required=True, action='append')
    requiredNamed.add_argument("--outputDir",         type=str,    help="The path where to write the output files", required=True)
    requiredNamed.add_argument("--outputFilename",    type=str,    help="The the name of the file to write to", required=True)

    return parser

def buildTravelOptions(args):
    travelOptions = TravelOptions()
    for source in args.source:
        travelOptions.addSource({
            "id" : str(source[0]) + ";" + str(source[1]),
            "lat" : source[0],
            "lng" : source[1],
            "tm" : { args.travelType : { "date" : args.date, "time" : args.time }}
        })
    travelOptions.setServiceKey(args.serviceKey)
    travelOptions.setTravelTimes(args.travelTimes)
    travelOptions.setTravelType(TravelType.parse(args.travelType))
    travelOptions.setServiceUrl(args.serviceUrl)
    if args.date:
        travelOptions.setTravelDate(args.date)
    if args.time:
        travelOptions.setTravelTime(args.time)
    if args.buffer:
        travelOptions.setBuffer(args.buffer)
    if args.simplify:
        travelOptions.setSimplifyMeter(args.simplify)
    if args.srid:
        travelOptions.setSrid(args.srid)
    if args.quadrantSegments:
        travelOptions.setQuadrantSegments(args.quadrantSegments)
    if args.polygonSerializer:
        travelOptions.setPolygonSerializationType(PolygonSerializationType.parse(args.polygonSerializer))
    if args.edgeWeightType:
        travelOptions.setEdgeWeightType(EdgeWeightType.parse(args.edgeWeightType))
    if args.minHoleSize:
        travelOptions.setMinPolygonHoleSize(args.minHoleSize)
    if args.frameDuration:
        travelOptions.setFrameDuration(args.frameDuration)
    if args.reverse:
        travelOptions.setReverse(args.reverse)
    if args.bikeSpeed:
        travelOptions.setBikeSpeed(args.bikeSpeed)
    if args.bikeUphill:
        travelOptions.setBikeUphill(args.bikeUphill)
    if args.bikeDownhill:
        travelOptions.setBikeDownhill(args.bikeDownhill)
    if args.walkSpeed:
        travelOptions.setWalkSpeed(args.walkSpeed)
    if args.walkUphill:
        travelOptions.setWalkUphill(args.walkUphill)
    if args.walkDownhill:
        travelOptions.setWalkDownhill(args.walkDownhill)

    return travelOptions

def getPolygons(travelOptions):
    polygons = ServiceExecutor().execute_service(travelOptions, "polygon")
    return polygons

def main():
    logging.basicConfig()
    parser = createParser()
    args = parser.parse_args()
    travelOptions = buildTravelOptions(args)
    polygons = getPolygons(travelOptions)    

    f = open(args.outputDir + args.outputFilename, 'w')
    f.write(json.dumps(polygons["data"]))

if __name__ == '__main__':
    main()
