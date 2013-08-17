__author__ = 'William'
import math

class CoordinateCalculations:
    """ A class to do necessary calculations
    on lat/long coord data"""

    __earthRadius = 6371

    def calculateDistance(self, long1, lat1, long2, lat2):
        """ Calculate distance between 2 coordinates
        Source for algorithm
        http://www.movable-type.co.uk/scripts/latlong.html"""
        degreesLat = math.radians(lat2 - lat1)
        degreesLong = math.radians(long2 - long1)
        lat1 = math.radians(lat1)
        lat2 = math.radians(lat2)
        a = math.sin(degreesLat/2.) * math.sin(degreesLat/2.) \
            + math.sin(degreesLong/2.) * math.sin(degreesLong/2.) * math.cos(lat1) * math.cos(lat2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = self.__earthRadius * c
        return d


