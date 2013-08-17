__author__ = 'William'
import os
from Logic.CoordinateCalculations import *
from Logic.GPXparser import *
from Impl.Visual import *


def main():
    coord = CoordinateCalculations()
    print(coord.calculateDistance(-9.3753420, 52.3070590, -9.3760000, 52.3066350))
    parser = GPXparser()
    data = parser.load(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sample.gpx')))
    collection = parser.createCollectionOfTrackPoints(data)
    for i in range(len(collection)):
        print "Time: " + collection[i].time + " Elev: " + collection[i].elevation
    visual = Visual()
    visual.update()


if __name__ == "__main__":main()