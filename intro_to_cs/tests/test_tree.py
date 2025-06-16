import unittest
from psets.tree import Node, check_node, find_tree_height

class TestTree(unittest.TestCase):
   def test_valid_input(self):
      result = 1
      tree1 = Node(8, Node(2, Node(1), Node(6)), Node(10))
      self.assertEqual(tree1.get_left_child().get_left_child().get_value(), result)

   def test_return_none(self):
      tree3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26))))
      self.assertIsNone(tree3.get_left_child().get_left_child().get_right_child())

   def test_deep_path(self):
      result = 26
      tree3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26))))
      self.assertEqual(tree3.get_right_child().get_right_child().get_right_child().get_value(), result)

   def test_not_equal(self):
      result = 24
      tree3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26))))
      self.assertNotEqual(tree3.get_right_child().get_right_child().get_right_child().get_value(), result)

   def test_node_exists(self):
      result = "No node"
      tree3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26))))
      node = tree3.get_left_child().get_left_child().get_right_child()
      self.assertEqual(check_node(node), result)

   def test_tree_height(self):
      result = 2
      tree1 = Node(8, Node(2, Node(1), Node(6)), Node(10))
      self.assertEqual(find_tree_height(tree1), result)

