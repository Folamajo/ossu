import unittest
from intro_to_cs.psets.pset_3 import text_to_list

class TestTextToList(unittest.TestCase):
   def test_valid_input(self):
      result = ['Hello', 'how', 'are', 'you']
      self.assertEqual(text_to_list("Hello how are you") == result)
