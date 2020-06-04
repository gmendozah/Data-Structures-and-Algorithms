import math
from queue import PriorityQueue


def shortest_path(M, start, goal):
    """
    M: represents the map input.
    start: represents the start node from which we start.
    goal: represents the node to which we have to get.
    """
    queue = PriorityQueue()
    queue.put(start, 0)
    
    prev = {start: None}
    costs = {start: 0}
    
    
    while not queue.empty():
        current = queue.get()
        
        if current == goal:
            generatePath(prev, start, goal)
            
        for node in M.roads[current]:
            straight_distance = distance(M.intersections[current], M.intersections[node])
            new_cost = costs[current] + straight_distance
            
            if node not in costs or new_cost < costs[node]:
                costs[node] = new_cost
                total_cost = new_cost + straight_distance
                queue.put(node, total_cost)
                prev[node] = current
                
    return generatePath(prev, start, goal)


def distance(start, goal):
    #returns ditance from start node to goal node
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))


def generatePath(prev, start, goal):
    current = goal
    path = [current]
    
    while current != start:
        current = prev[current]
        path.append(current)
        
    path.reverse()
    
    return path