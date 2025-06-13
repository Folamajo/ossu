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
   
print(check_node(node))