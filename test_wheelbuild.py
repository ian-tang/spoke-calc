import unittest
import wheelbuild

class WheelBuildTest(unittest.TestCase):
    # test valid cases
    def test_radialLace(self):
        self.assertAlmostEqual(282.4, wheelbuild.calc_spoke_length(45, 55, 599, 36, 0), delta = 0.05)
    def test_cross1(self):
        self.assertAlmostEqual(281.2, wheelbuild.calc_spoke_length(50, 43, 590, 16, 1), delta = 0.05)
    def test_cross2(self):
        self.assertAlmostEqual(283.4, wheelbuild.calc_spoke_length(50, 43, 590, 28, 2), delta = 0.05)
    def test_cross3(self):
        self.assertAlmostEqual(289.6, wheelbuild.calc_spoke_length(50, 43, 590, 32, 3), delta = 0.05)
    def test_cross4(self):
        self.assertAlmostEqual(291.4, wheelbuild.calc_spoke_length(50, 43, 590, 40, 4), delta = 0.05)
    
    # test invalid inputs
    def test_invalidFlangeDiameter(self):
        self.assertRaises(ValueError, wheelbuild.calc_spoke_length, 400, 66, 350, 36, 0)
    def test_invalidSpokeCount(self):
        self.assertRaises(ValueError, wheelbuild.calc_spoke_length, 45, 55, 599, 33, 0)
    def test_invalidLacingPattern(self):
        self.assertRaises(ValueError, wheelbuild.calc_spoke_length, 45, 55, 599, 36, 5)
    
    # test negative inputs
    def test_negativeFlangeDiameter(self):
        self.assertRaises(ValueError, wheelbuild.calc_spoke_length, -45, 55, 599, 36, 3)
    def test_negativeCenterFlangeDistance(self):
        self.assertRaises(ValueError, wheelbuild.calc_spoke_length, 45, -55, 599, 36, 3)
    def test_negativeERD(self):
        self.assertRaises(ValueError, wheelbuild.calc_spoke_length, 45, 55, -500, 36, 5)
    def test_negativeSpokeCount(self):
        self.assertRaises(ValueError, wheelbuild.calc_spoke_length, 45, 55, 599, -36, 3)
    def test_negativeLacingPattern(self):
        self.assertRaises(ValueError, wheelbuild.calc_spoke_length, 45, 55, 599, 36, -3)
