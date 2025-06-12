import unittest
from psets.tree import Node

class TestTreeOne(unittest.TestCase):
   def test_valid_input(self):
      result = 1
      tree1 = Node(8, Node(2, Node(1), Node(6)), Node(10))
      self.assertEqual(tree1.get_left_child().get_left_child().get_value(), result)