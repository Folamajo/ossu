import unittest
from ..psets.pset_0 import get_power_of


class TestGetPowerOf(unittest.TestCase):
   def test_get_power_of(self):
      result = 0.00390625
      self.assertAlmostEqual(get_power_of(4, -4), result, places = 6)