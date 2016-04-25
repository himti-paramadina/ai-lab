class BinaryTreeNode:

  def __init__(self, key, value):
    self.key = key
    self.value = value

    self.left = None
    self.right = None
    self.parent = None


class BinaryHeap:

  def __init__(self):
    self.keys = []
    self.values = {}

  def _bubble_up(self, i):
    while (i - 1) // 2 >= 0:
      parent_index = (i - 1) // 2
      if (self.keys[i] < self.keys[parent_index]):
        tmp = self.keys[parent_index]
        self.keys[parent_index] = self.keys[i]
        self.keys[i] = tmp
      i = parent_index

  def insert(self, key, value):
    self.keys.append(key)
    self.values[key] = value
    self._bubble_up(len(self.keys) - 1)

    print self.keys

  def _inorder(self, i, callback):
    if (i < len(self.keys)):
      self._inorder(2 * i + 1, callback)
      callback(i, self.keys[i], self.values[self.keys[i]])
      self._inorder(2 * i + 2, callback)

  def traverse_inorder(self, callback):
    self._inorder(0, callback)

  def _preorder(self, node, callback):
    print 'Unimplemented.'

  def traverse_preorder(self, callback):
    print 'Unimplemented.'

  def _postorder(self, node, callback):
    print 'Unimplemented.'

  def traverse_postorder(self, callback):
    print 'Unimplemented.'

  def delete(self, lookup_value):
    print 'Unimplemented.'


class BinarySearchTree:

  def __init__(self):
    self.root = None

  def insert(self, key, value):
    current_node = self.root

    if (current_node is None):
      self.root = BinaryTreeNode(key, value)
    else:
      not_found = True
      while (not_found):
        previous_node = current_node
        position = None
        if (key < current_node.key):
          current_node = current_node.left
          position = 'left'
        else:
          current_node = current_node.right
          position = 'right'

        if (current_node is None):
          current_node = BinaryTreeNode(key, value)
          current_node.parent = previous_node
          if (position == 'left'):
            previous_node.left = current_node
          else:
            previous_node.right = current_node

          not_found = False

  def delete(self, key):
    print 'Unimplemented.'

  def find(self, key):
    if (self.root is None):
      return None
    else:
      current_node = self.root
      while (current_node is not None):
        if (node.key == current_node.key):
          return current_node
        elif (node.key < current_node.key):
          current_node = current_node.left
        elif (node.key > current_node.key):
          current_node = current_node.right

      return None

  def _inorder(self, node, callback):
    if (node is not None):
      self._inorder(node.left, callback)
      callback(node)
      self._inorder(node.right, callback)

  def traverse_inorder(self, callback):
    self._inorder(self.root, callback)

  def _preorder(self, node, callback):
    if (node is not None):
      callback(node)
      self._preorder(node.left, callback)
      self._preorder(node.right, callback)

  def traverse_preorder(self, callback):
    self._preorder(self.root, callback)

  def _postorder(self, node, callback):
    if (node is not None):
      self._postorder(node.left, callback)
      self._postorder(node.right, callback)
      callback(node)

  def traverse_postorder(self, callback):
    self._postorder(self.root, callback)
