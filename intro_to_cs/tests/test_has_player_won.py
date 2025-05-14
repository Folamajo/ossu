import unittest
from intro_to_cs.psets.pset_2 import has_player_won

class TestHasPlayerWon(unittest.TestCase):

   def test_invalid_input(self):
      with self.assertRaises(TypeError):
         has_player_won(123, ["a","b","c"])

   def test_valid_win(self):
      self.assertEqual(has_player_won("apple", ["b", "a", "d", "p", "l", "e"]), True)

   def test_valid_loss(self):
      self.assertEqual(has_player_won("apple", ["b", "k", "r"]), False)