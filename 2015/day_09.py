from pathlib import Path
from collections import defaultdict

with open(Path('2015','day_09.txt')) as file:
    all_line = [row for row in file.read().replace(" = ", ' ').replace(" to ", " ").split('\n')]
    all_line = [item.split() for item in all_line]


class Graph():

    def __init__(self):
        self.all_nodes = {}
        self.all_route_distance = []

    def add_node(self, name):
        if name not in self.all_nodes:
            self.all_nodes[name] = Node(name)
    
    def add_node_link(self, source, destination, distance):
        if source in self.all_nodes and destination in self.all_nodes:
            self.all_nodes[source].add_link(self.all_nodes[destination], distance)

    def resolve(self):
        self.all_route_distance = []
        for node in self.all_nodes.values():
            node.resolve(0)

class Node():
    def __init__(self, name):
        self.name = name
        self.links = {}
        self.visited = False
    
    def add_link(self, destination, distance):
        if destination.name not in self.links:
            self.links[destination.name] = [destination, distance]
            destination.add_link(self, distance)
    
    def visit(self):
        self.visited = True
    
    def unvisit(self):
        self.visited = False

    def is_visited(self):
        return self.visited

    def resolve(self, partial_distance):
        self.visit()
        visited_destinarion = []
        for destination, distance in self.links.values():
            visited_destinarion.append(destination.is_visited())
            if not destination.is_visited():
                destination.resolve(partial_distance + distance)
        if False not in visited_destinarion:
            graph.all_route_distance.append(partial_distance)
        self.unvisit()
 
graph = Graph()

for route in all_line:
    dest_1 = route[0]
    dest_2 = route[1]
    distance = int(route[2])

    graph.add_node(dest_1)
    graph.add_node(dest_2)
    graph.add_node_link(dest_1, dest_2, distance)
    
graph.resolve()

print(min(graph.all_route_distance))
print(max(graph.all_route_distance))

