from typing import Optional

class Node:
   def __init__(self, value:int, left_child: Optional['Node'], right_child: Optional['Node']):
      self.value = value
      self.left_child = left_child
      self.right_child = right_child

   