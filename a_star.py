# encoding:utf-8

# This file implements "A star" algorithm - Author: Marcos Castro

# A* or "A star" is the combination of Uniform-cost and Greedy
# Uniform-cost orders by path cost or backward cost - g(n)
# Greedy orders by goal proximity or forward cost - h(n)
# A* Search orders by the sum: f(n) = g(n) + h(n)
# Reference: https://www.youtube.com/watch?v=b9fH-j_yNHU

import heapq # priority queue
from collections import defaultdict # dictionary of lists


# class that represents a priority queue
class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def insert(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def remove(self):
        return heapq.heappop(self._queue)[-1]

    def isEmpty(self):
        return len(self._queue) == 0

    def getSize(self):
        return self._index


# class that represents a node
class Node:

    # "key" is the identifier of node
    # "forward_cost" is h(n) (cost of the heuristic)
    # "forward_cost" is used in the calculate of "A* search": f(n) = g(n) + h(n) where
    # h(n) is the forward cost and g(n) is the backward cost
    # remember: "A* search" is the combination of Uniform-cost (UCS) and Greedy
    def __init__(self, key, forward_cost):
        self.key = key
        self.forward_cost = forward_cost

    def getKey(self):
        return self.key

    def getForwardCost(self):
        return self.forward_cost


# class that represents a graph
class Graph:

    def __init__(self):
        self.nodes = {} # dictionary of the nodes
        self.edges = [] # list of 3-tuple (source, destination, weight)
        self.path = [] # path

        # dictionary with the lists of successors of each node, faster for get the successors
        # each item of list is a 2-tuple: (destination, weight)
        self.successors = defaultdict(list)


    # function that adds edges
    def addEdge(self, source, destination, weight):
        edge = (source, destination, weight) # creates tuple (3-tuple)
        if not self.existsEdge(edge): # adds edge if not exists
            self.nodes[source], self.nodes[destination] = source, destination # adds the nodes
            self.edges.append(edge) # adds edge
            self.successors[source.getKey()].append((destination, weight)) # adds successor
        else:
            print('Error: edge (%s -> %s with weight %s) already exists!!' \
                % (edge[0].getKey(), edge[1].getKey(), edge[2]))


    # function that checks if edge exists
    def existsEdge(self, edge):
        for e in self.edges:
            # compares source's key, destionation's key and weight of edge
            if e[0].getKey() == edge[0].getKey() and \
                e[1].getKey() == edge[1].getKey() and e[2] == edge[2]:
                return True
        return False


    # function that returns the path
    def getPath(self):
        return self.path


    # function that run the "A*" algorithm
    def executeAStar(self, initial_node, goal_node):
        if not self.edges:
            print('Error: graph not contains edges!!')
        else:
            # checks if both the nodes exists
            if initial_node in self.nodes and goal_node in self.nodes:
                if initial_node == goal_node: # checks if are the same nodes
                    return 0

                queue = PriorityQueue() # creates a priority queue (min heap)

                # "distance_vector" and "antecessors" are used for reconstruct the path
                distance_vector, antecessors = {}, {}
                for node in self.nodes:
                    distance_vector[node.getKey()] = None # initializes with None
                    antecessors[node.getKey()] = None
                distance_vector[initial_node.getKey()] = 0

                # calculates costs
                g_cost, h_cost = 0, initial_node.getForwardCost()
                f_cost = g_cost + h_cost
                queue.insert((initial_node, g_cost, h_cost), f_cost)
                total_cost = None

                while True:

                    # a item of the queue is a 3-tuple: (current_node, g_cost, h_cost)
                    current_node, g_cost, h_cost = queue.remove()

                    # gets all the successors of "current_node"
                    successors = self.successors[current_node.getKey()]

                    for successor in successors:
                        destination, weight = successor # unpack 2-tuple successor

                        # calculates costs
                        new_g_cost = g_cost + weight
                        h_cost = destination.getForwardCost()
                        f_cost = new_g_cost + h_cost
                        queue.insert((destination, new_g_cost, h_cost), f_cost)

                        # updates "distance_vector"
                        if distance_vector[destination.getKey()]:
                            if distance_vector[destination.getKey()] > new_g_cost:
                                distance_vector[destination.getKey()] = new_g_cost
                                antecessors[destination.getKey()] = current_node.getKey()
                        else:
                            distance_vector[destination.getKey()] = new_g_cost
                            antecessors[destination.getKey()] = current_node.getKey()

                        # verifies that reached the goal
                        if destination.getKey() == goal_node.getKey():
                            # updated "total_cost"
                            if not total_cost:
                                total_cost = f_cost
                            elif f_cost < total_cost:
                                total_cost = f_cost

                    if queue.isEmpty(): # verifies if the queue is empty
                        # reconstruct the path
                        curr_node = goal_node.getKey()
                        while curr_node:
                            self.path.append(curr_node)
                            curr_node = antecessors[curr_node]
                        self.path = self.path[::-1]
                        return total_cost
            else:
                print('Error: the node(s) not exists in the graph!!')


# tests ...

# First Example - Graph 1 ("graph1.png" is in "images" folder in repository)

# creates the nodes
nodeS = Node('S', 3)
nodeA = Node('A', 2)
nodeB = Node('B', 1)
nodeG = Node('G', 0)

# creates graph
graph = Graph()

# add the edges
graph.addEdge(nodeS, nodeA, 2)
graph.addEdge(nodeS, nodeB, 2)
graph.addEdge(nodeA, nodeG, 2)
graph.addEdge(nodeB, nodeG, 3)

total_cost = graph.executeAStar(nodeS, nodeG) # executes the algorithm
path = graph.getPath() # gets path
if total_cost:
    print('Total cost of graph 1: %s. Path: %s' % (total_cost, ' -> '.join(path)))
else:
    print('Did not reach the goal!')


# Second Example - Graph 2 ("graph2.png" is in "images" folder in repository)

nodeS = Node('S', 6)
nodeA = Node('A', 5)
nodeB = Node('B', 6)
nodeC = Node('C', 7)
nodeE = Node('E', 1)
nodeD = Node('D', 2)
nodeG = Node('G', 0)

graph2 = Graph()
graph2.addEdge(nodeS, nodeA, 1)
graph2.addEdge(nodeA, nodeB, 1)
graph2.addEdge(nodeB, nodeC, 1)
graph2.addEdge(nodeA, nodeE, 8)
graph2.addEdge(nodeA, nodeD, 3)
graph2.addEdge(nodeE, nodeD, 2)
graph2.addEdge(nodeD, nodeG, 2)

total_cost = graph2.executeAStar(nodeS, nodeG)
path = graph2.getPath()
if total_cost:
    print('Total cost of graph 2: %s. Path: %s' % (total_cost, ' -> '.join(path)))
else:
    print('Did not reach the goal!')