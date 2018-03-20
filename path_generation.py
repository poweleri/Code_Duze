import numpy as np
from operator import itemgetter, attrgetter
#from sets import set
from room import Room
import config

class Node(object):
	def __init__(self, room):
		self.room = room
		self.connections = set()
		self.connections.add(room)
		
class Edge (object):
	def __init__(self, nodeA, nodeB):
		self.A = nodeA
		self.B = nodeB
		centerA = np.array(self.A.room.shape.center)
		centerB = np.array(self.B.room.shape.center)
		self.distance = np.linalg.norm(centerA-centerB)
		
class GraphNode(object):
	def __init__(self, node):
		self.room = node.room
		self.edges = []
		
	def addEdge(self, node):
		self.edges.append(node.room)
		
def createNodes(rooms):
	nodes = []
	for x in rooms:
		node = Node(x)
		nodes.append(node)
		# x.roomInfo()
	return nodes
	
def getEdges(nodes):
	edges = []
	for x in xrange(len(nodes)):
		for y in xrange(x+1, len(nodes)):
			edge = Edge(nodes[x], nodes[y])
			# print ("-- From --")
			# nodes[x].room.roomInfo()
			# print ("-- To --")
			# nodes[y].room.roomInfo()
			# print ()
			# print (edge.distance)
			edges.append(edge)
	return edges			
	
def allConnected(nodes):
	for x in nodes:
		if (not x.connected):
			return False
	return True
	
# Returns a list of list rooms, the first item in each
# list is the base node, and the subsequent elements are 
# edges that room has to other rooms
def createMST(rooms):	
	nodes = createNodes(rooms)
	edges = getEdges(nodes)
	
	tempGraph = []
	compareSet = set()
	
	for x in nodes:
		compareSet.add(x)
	
	# Using Kruskal's algorithm to find the MST
	edges = sorted(edges, key=attrgetter('distance'))
	
	for x in edges:
		if (x.A.connections != compareSet):
			if ((x.A.connections <= (x.A.connections - x.B.connections)) and (x.B.connections <= (x.B.connections - x.A.connections))):
				tempGraph.append(x)
				x.A.connections = x.A.connections | x.B.connections
				x.B.connections = x.A.connections | x.B.connections
		else:
			break

	graph = []
	
	for x in nodes:
		temp = GraphNode(x)
		for y in tempGraph:	
			if (x == y.A):
				temp.addEdge(y.B)
				tempGraph.remove(y)
			elif (x == y.B):
				temp.addEdge(y.A)
				tempGraph.remove(y)		
		graph.append(temp)	
		
	return graph
