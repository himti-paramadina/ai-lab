class BinaryHeapNode:

  def __init__(self, value):
    self.value = value

    self.left = None
    self.right = None
    self.parent = None

  def set_left(self, node):
    self.left = node

  def set_right(self, node):
    self.right = node

  def set_parent(self, node):
    self.parent = parent


class BinarySearchTreeNode:

  def __init__(self, value, left=None, right=None, parent=None):
    self.value = value

    self.left = left
    self.right = right
    self.parent = parent

  def set_left(self, node):
    self.left = node

  def set_right(self, node):
    self.right = node

  def set_parent(self, node):
    self.parent = parent


class BinaryHeap:

  def __init__(self, size=0)
    self.values = []
    if (size is not 0):
      for i in range(len(size)):
        self.values.append(None)

  def insert(self, node):

  def delete(self, lookup_value):


class BinarySearchTree:

  def __init__(self):
    self.root = None

  def insert(self, node):
    if (self.root is None):
      self.root = node
    else:
      node = self.root

  def delete(self, node):

  def find(self, value):
