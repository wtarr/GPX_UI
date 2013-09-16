__author__ = 'William'
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
from Logic.CoordinateCalculations import *

class TestCoordinateCalculations(unittest.TestCase):

    def setUp(self):
        self.coordcalc = CoordinateCalculations()

    def test_calculateDistance(self):
        dist = self.coordcalc.calculateDistance(-9.3753420, 52.3070590, -9.3760000, 52.3066350)
        self.assertAlmostEquals(dist, 0.06499, places=5)