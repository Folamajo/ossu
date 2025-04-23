import unittest
from intro_to_cs.psets.pset_1 import saving_with_raise

class TestSavingWithRaise(unittest.TestCase):
   def test_calculate_saving_with_raise(self):
      result = 92
      self.assertEqual(saving_with_raise(110000, 0.15, 750000, 0.03), result)