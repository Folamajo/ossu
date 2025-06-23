from typing import Optional

class Node:
   def __init__(self, value:int , left_child: Optional['Node'] = None, right_child: Optional['Node'] = None):
      self.value = value
      self.left_child = left_child
      self.right_child = right_child

   def get_value(self):
      return self.value
   
   def get_left_child(self):
      return self.left_child
   
   def get_right_child(self):
      return self.right_child


tree1 = Node(8, Node(2, Node(1), Node(6)), Node(10))
tree2 = Node(7, Node(2, Node(1), Node(5, Node(3), Node(6))), Node(9, Node(8), Node(10)))
tree3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26))))

node = tree3.get_left_child().get_left_child().get_right_child()

def check_node(input):
   if input is not None :
      return input.get_value()
   else:
      return "No node"
   


def find_tree_height(node):
   if node == None:
      return -1

 
   return 1 + max(find_tree_height(node.get_left_child()), find_tree_height(node.get_right_child()))
   

# def compare_func(child_value, parent_value):
#    if child_value > parent_value:
#       return "min_heap"
   
#    elif child_value < parent_value:
#       return "max_heap"

def max_heap_comparator(child_value, parent_value):
   if child_value < parent_value:
      return True
   return False

def min_heap_comparator(child_value, parent_value):
   if child_value > parent_value:
      return True
   return False




max_heap_node = Node(21, Node(15, Node(7), Node(11)), Node(3, Node(2), Node(1)))

def is_heap(tree, compare_func):
   if tree == None:
      return True
   

   if tree.get_left_child():
      if not compare_func(tree.get_left_child().get_value(), tree.get_value()):
         return False
      else:
         if not is_heap(tree.get_left_child(), compare_func):
            return False

      # result_one = is_heap(tree, max_heap_comparator(tree.get_value(), tree.get_left_child().get_value()))
   if tree.get_right_child():
      if not compare_func(tree.get_right_child().get_value(), tree.get_value()):
         return False
      else:
         if not is_heap(tree.get_right_child(), compare_func):
            return False
   
   return True

print(is_heap(max_heap_node, min_heap_comparator))