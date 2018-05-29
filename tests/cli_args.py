from config import *

REQUIRED_CORE_ARGS = [
    '--travelTimes', '300', '600', 
    '--travelType', 'walk', 
    '--source', '52.52;13.405', 
    '--outputDir', 'data/', 
    '--outputFilename', 'core_args_output.geojson',
    '--serviceKey', API_KEY,
    '--serviceUrl', 'http://service.targomo.com/germany/'
]

FULL_ARGS = [
    '--travelTimes', '300', '600', 
    '--travelType', 'transit', 
    '--source', '52.52;13.405', 
    '--outputDir', 'data/', 
    '--outputFilename', 'full_args_output.geojson',
    '--serviceKey', API_KEY,
    '--serviceUrl', 'http://service.targomo.com/germany/',
    '--minHoleSize', '10000000',
    '--time', '28800',
    '--date', '20170101',
    '--polygonSerializer', 'geojson',
    '--edgeWeightType', 'distance',
    '--buffer', '0.002',
    '--simplify', '10',
    '--srid', '4326',
    '--quadrantSegments', '6',
    '--frameDuration', '3600',
    '--reverse', 'True',
    '--bikeSpeed', '15',
    '--bikeUphill', '1.2',
    '--bikeDownhill', '.8',
    '--walkSpeed', '5',
    '--walkUphill', '1.1',
    '--walkDownhill', '.9'
]

FULL_ARGS_TRANSIT = [
    '--travelTimes', '300', '600', 
    '--travelType', 'transit', 
    '--source', '52.52;13.405', 
    '--outputDir', 'data/', 
    '--outputFilename', 'full_args_output.geojson',
    '--serviceKey', API_KEY,
    '--serviceUrl', 'http://service.targomo.com/germany/',
    '--minHoleSize', '10000000',
    '--time', '28800',
    '--date', '20170101',
    '--polygonSerializer', 'geojson',
    '--edgeWeightType', 'time',
    '--buffer', '0.002',
    '--simplify', '10',
    '--srid', '4326',
    '--quadrantSegments', '6',
    '--frameDuration', '3600',
    '--reverse', 'True'
]