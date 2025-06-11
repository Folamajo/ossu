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


tree1 = Node(1, Node(2), Node(5, Node(7), Node(8)))
tree2 = Node(7, Node(2, Node(1), Node(5, Node(3), Node(6))), Node(9, Node(8), Node(10)))
# print(tree1.get_right_child().get_left_child().get_value())

node = tree1.get_left_child().get_left_child()
# print(node)
if node is not None :
   print(node.get_value())
else:
   print("No node")