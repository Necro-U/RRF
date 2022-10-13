from utilities.VertexManager import VertexManager
from utilities.vertex import Vertex
from utilities.vector import Vector


a = Vector([12, 12])
b = Vector([25, 25])
a = Vertex(a)
b = Vertex(b)
# print((a - b).distance)
manager = VertexManager()
manager.add_vertex(a)
manager.add_vertex(b)
manager.find_closest_vertex(Vertex(Vector([13, 13])))
