import unittest
from intro_to_cs.psets.pset_3 import text_to_list, get_frequencies, get_letter_frequencies

class TestTextToList(unittest.TestCase):
   def test_valid_input(self):
      result = ['Hello', 'how', 'are', 'you']
      self.assertEqual(text_to_list("Hello how are you"), result)

   def test_invalid_input_type(self):
      with self.assertRaises(TypeError):
         text_to_list(123)
      

   def test_empty_string(self):
      result = []
      self.assertEqual(text_to_list(""), result)

   
class TestGetFrequencies(unittest.TestCase):
   def test_valid_input(self):
      result = {'hello' : 2,
                'hi': 1}
      self.assertEqual(get_frequencies(["hello", "hello", "hi"]), result )

   def test_invalid_input_type(self):
      with self.assertRaises(TypeError):
         get_frequencies(["hello", 123])

   def test_empty_list(self):
      result = {}
      self.assertEqual(get_frequencies([]), result)

class TestGetLetterFrequencies(unittest.TestCase):
   def test_valid_input(self):
      result = {'h': 1, 'i': 1}
      self.assertEqual(get_letter_frequencies('hi'), result)

   def test_invalid_input_type(self):
      with self.assertRaises(TypeError):
         get_letter_frequencies(1)

   def test_empty_string(self):
      result = {}
      self.assertEqual(get_letter_frequencies(""), result)