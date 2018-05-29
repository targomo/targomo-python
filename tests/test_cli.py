from config import *
from cli_args import *
from targomo_python.cli.__main__ import createParser, buildTravelOptions, getPolygons
from targomo_python.util.enum.PolygonSerializationType import PolygonSerializationType
from targomo_python.util.enum.TravelType import TravelType
from unittest import TestCase
import json

class CommandLineTestCase(TestCase):
    """
    Base TestCase class, sets up a CLI parser
    """
    @classmethod
    def setUpClass(cls):
        parser = createParser()
        cls.parser = parser

class CliTestCase(CommandLineTestCase):
    def test_with_empty_args(self):
        """
        User passes no args, should fail with SystemExit
        """                              
        with self.assertRaises(SystemExit):
            self.parser.parse_args([])

    def test_travel_options_required(self):
        """
        Travel Options created with required args
        """
        args = self.parser.parse_args(REQUIRED_CORE_ARGS)

        travelOptions = buildTravelOptions(args)
        self.assertIsNotNone(travelOptions, 'Should succeed in creating travelOptions')
        self.assertListEqual(travelOptions.getTravelTimes(), [300,600], 'Should properly assign travel times to travelOptions')
        self.assertEqual(travelOptions.getSources()[0]['lat'], 52.52, 'Should properly assign source lat to travelOptions.sources')
        self.assertEqual(travelOptions.getSources()[0]['lng'], 13.405, 'Should properly assign source lng to travelOptions.sources')
        self.assertEqual(travelOptions.getTravelType().value, 'walk', 'Should properly assign travel type to travelOptions')
        self.assertEqual(travelOptions.getServiceKey(), API_KEY, 'Should properly assign service key to travelOptions')
        self.assertEqual(travelOptions.getServiceUrl(), 'http://service.targomo.com/germany/', 'Should properly assign service url to travelOptions')

    def test_polygon_required_args(self):
        """
        Polygon created with required args
        """
        args = self.parser.parse_args(REQUIRED_CORE_ARGS)

        travelOptions = buildTravelOptions(args)
        polygons = getPolygons(travelOptions)
        self.assertIsNotNone(polygons, 'Should succeed in creating polygons')

    def test_travel_options_full(self):
        """
        Travel Options created with full args
        """
        args = self.parser.parse_args(FULL_ARGS)

        travelOptions = buildTravelOptions(args)
        self.assertIsNotNone(travelOptions, 'Should succeed in creating travelOptions')
        self.assertListEqual(travelOptions.getTravelTimes(), [300,600], 'Should properly assign travel times to travelOptions')
        self.assertEqual(travelOptions.getSources()[0]['lat'], 52.52, 'Should properly assign source lat to travelOptions.sources')
        self.assertEqual(travelOptions.getSources()[0]['lng'], 13.405, 'Should properly assign source lng to travelOptions.sources')
        self.assertEqual(travelOptions.getTravelType().value, 'transit', 'Should properly assign travel type to travelOptions')
        self.assertEqual(travelOptions.getServiceKey(), API_KEY, 'Should properly assign service key to travelOptions')
        self.assertEqual(travelOptions.getServiceUrl(), 'http://service.targomo.com/germany/', 'Should properly assign service url to travelOptions')
        self.assertEqual(travelOptions.getMinPolygonHoleSize(), 10000000, 'Should properly assign min hole size to travelOptions')
        self.assertEqual(travelOptions.getTravelTime(), 28800, 'Should properly assign travel time to travelOptions')
        self.assertEqual(travelOptions.getTravelDate(), 20170101, 'Should properly assign travel date to travelOptions')
        self.assertEqual(travelOptions.getPolygonSerializationType().value, 'geojson', 'Should properly assign polygon serializer to travelOptions')
        self.assertEqual(travelOptions.getBuffer(), 0.002, 'Should properly assign buffer to travelOptions')
        self.assertEqual(travelOptions.getSimplifyMeter(), 10, 'Should properly assign simplification threshold to travelOptions')
        self.assertEqual(travelOptions.getSrid(), 4326, 'Should properly assign travel date to travelOptions')
        self.assertEqual(travelOptions.getQuadrantSegments(), 6, 'Should properly assign quadrant segments to travelOptions')
        self.assertEqual(travelOptions.getTravelDate(), 20170101, 'Should properly assign travel date to travelOptions')
        self.assertEqual(travelOptions.getFrameDuration(), 3600, 'Should properly assign frame duration to travelOptions')
        self.assertEqual(travelOptions.getReverse(), True, 'Should properly assign reverse to travelOptions')
        self.assertEqual(travelOptions.getWalkSpeed(), 5, 'Should properly assign walk speed to travelOptions')
        self.assertEqual(travelOptions.getWalkUphill(), 1.1, 'Should properly assign uphill walk penalty to travelOptions')
        self.assertEqual(travelOptions.getWalkDownhill(), .9, 'Should properly assign downhill walk penalty to travelOptions')
        self.assertEqual(travelOptions.getBikeSpeed(), 15, 'Should properly assign bike speed to travelOptions')
        self.assertEqual(travelOptions.getBikeUphill(), 1.2, 'Should properly assign uphill bike penalty to travelOptions')
        self.assertEqual(travelOptions.getBikeDownhill(), .8, 'Should properly assign downhill bike penalty to travelOptions')

    def test_polygon_full_transit(self):
        """
        Polygon created with full args - transit
        """
        args = self.parser.parse_args(FULL_ARGS_TRANSIT)

        travelOptions = buildTravelOptions(args)
        polygons = getPolygons(travelOptions)
        self.assertIsNotNone(polygons, 'Should succeed in creating polygons')