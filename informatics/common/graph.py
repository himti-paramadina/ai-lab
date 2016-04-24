class GraphNode:

  def __init__(self, id, data={}):
    self.id = id
    self.data = data

  def get_id(self):
    return self.id

  def get_data(self):
    return self.data

  def set_data(self, data):
    self.data = data

class Graph:

  def __init__(self):
    self.adjacency_map = {}
    self.vertices = {}

  def add_vertex(self, node):
    self.vertices[node.id] = node
    self.adjacency_map[node.id] = {}

  def add_edge(self, node_id1, node_id2, data={}):
    current = self.adjacency_map[node_id1]
    if current is not None:
      self.adjacency_map[node_id1][node_id2] = data

  def get_vertex(self, id):
    return self.vertices[id]

  def get_vertices(self):
    vertices = []
    for id in self.vertices:
      vertices.append(self.vertices[id])
    return vertices

  def get_edge(self, node_id1, node_id2):
    if (node_id1 in self.adjacency_map):
      if (node_id2 in self.adjacency_map[node_id1]):
        return self.adjacency_map[node_id1][node_id2]
    return None

  def get_adjacent_vertices(self, node_id):
    adjacent_vertices = []
    for id in self.adjacency_map[node_id]:
      adjacent_vertices.append(self.vertices[node_id])
    return adjacent_vertices

  def is_adjacent(self, node_id1, node_id2):
    return (node_id1 in self.adjacency_map) and (node_id2 in self.adjacency_map[node_id1])
