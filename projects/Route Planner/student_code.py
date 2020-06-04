from math import cos, asin, sqrt, pi
import networkx as nx
import pickle


class Node:
    def __init__(self, _id, parent):
        self.id = _id
        self.parent = parent
        self.g = 0
        self.h = 0  # est. distance
        self.f = 0  # total


class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.length = 0

    def size(self):
        return self.length

    def is_empty(self):
        return self.length == 0

    def has_node(self, node):
        for i in range(self.length):
            if self.queue[i].id == node.id:
                return True
            break
        return False

    def put(self, node):
        # adding an element to the queue
        self.queue.append(node)
        self.length += 1

    def get(self):
        # deleting  least frequent node
        index = 0
        least_length_node = self.queue[index]

        for i in range(self.length):
            if self.queue[i].f < least_length_node.f:
                least_length_node = self.queue[i]
                index = i

        del self.queue[index]
        self.length -= 1

        return least_length_node


def shortest_path(M, start, goal):
    """
    M: represents the map input.
    start: represents the start node from which we start.
    goal: represents the node to which we have to get.

    To solve this problem, I followed Pseudocode from this post:
    https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
    """
    start_node = Node(start, None)

    queue = PriorityQueue()
    seen = set()

    queue.put(start_node)

    while not queue.is_empty():
        current = queue.get()
        seen.add(current.id)

        if current.id == goal:
            #print(F"------- break: {goal} -------")
            return build_route(current)

        #print(F"current: {current.id}")
        # print(F"frontier: {M.roads[current.id]}")
        for frontier_node in M.roads[current.id]:
            if frontier_node in seen:
                continue

            node = build_node(M, frontier_node, current, goal)

            if queue.has_node(node):
                continue
            queue.put(node)

    return []


def build_node(M, _id, parent, goal):
    # distance from child to parent (current)
    g = parent.g + distance(M.intersections[_id], M.intersections[parent.id])
    # distance from child to end
    h = distance(M.intersections[_id], M.intersections[goal])
    f = g + h
    node = Node(_id, parent)
    node.g = g
    node.h = h
    node.f = f
    return node


def distance(start, goal):
    """
    Haversine formula to determine distance between two points in a sphere given their latitudes and longitudes.
    https://en.wikipedia.org/wiki/Haversine_formula
    https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula
    """
    p = pi / 180
    a = 0.5 - cos((goal[0] - start[0]) * p) / 2 + cos(start[0] * p) * cos(goal[0] * p) * (
            1 - cos((goal[1] - start[1]) * p)) / 2
    return 12742 * asin(sqrt(a))


def build_route(current):
    path = []
    while current.parent is not None:
        path.append(current.id)
        current = current.parent
    path.append(current.id)
    path.reverse()
    return path


class Map:
    def __init__(self, G):
        self._graph = G
        self.intersections = nx.get_node_attributes(G, "pos")
        self.roads = [list(G[node]) for node in G.nodes()]

    def save(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self._graph, f)


def load_map(name):
    with open(name, 'rb') as f:
        G = pickle.load(f)
    return Map(G)


MAP_40_ANSWERS = [
    (5, 34, [5, 16, 37, 12, 34]),
    (5, 5, [5]),
    (8, 24, [8, 14, 16, 37, 12, 17, 10, 24])
]


def test(shortest_path_function):
    map_40 = load_map('map-40.pickle')
    correct = 0
    for start, goal, answer_path in MAP_40_ANSWERS:
        path = shortest_path_function(map_40, start, goal)
        if path == answer_path:
            correct += 1
        else:
            print("For start:", start,
                  "Goal:     ", goal,
                  "Your path:", path,
                  "Correct:  ", answer_path)
    if correct == len(MAP_40_ANSWERS):
        print("All tests pass! Congratulations!")
    else:
        print("You passed", correct, "/", len(MAP_40_ANSWERS), "test cases")


map_40 = load_map('map-40.pickle')


def test2():
    path = shortest_path(map_40, 5, 34)
    if path == [5, 16, 37, 12, 34]:
        print("great! Your code works for these inputs!")
    else:
        print("something is off, your code produced the following:")
        print(path)


test(shortest_path)
