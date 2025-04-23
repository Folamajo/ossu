import unittest
from intro_to_cs.psets.pset_1 import calculate_months_to_save, caluclate_months_with_raise


class TestCalculateMonthsToSave(unittest.TestCase):
   def test_calculate_months_to_save(self):
      result = 97 
      self.assertEqual(calculate_months_to_save(112000, 0.17, 750000), result)


class TestCalculateMonthsWithRaise(unittest.TestCase):
   def test_calculate_months_with_raise(self):
      result = 92
      self.assertEqual(caluclate_months_with_raise(110000, 0.15, 750000, 0.03), result)