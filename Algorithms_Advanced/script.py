import heapq
import math

def heuristic(a, b):
    # Euclidean distance
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def shortest_path(M, start, goal):
    intersections = M.intersections
    roads = M.roads

    frontier = []
    heapq.heappush(frontier, (0 + heuristic(intersections[start], intersections[goal]), 0, start, [start]))
    explored = set()
    cost_so_far = {start: 0}

    while frontier:
        _, cost, current, path = heapq.heappop(frontier)

        if current == goal:
            return path

        if current in explored:
            continue
        explored.add(current)

        for neighbor in roads[current]:
            new_cost = cost + heuristic(intersections[current], intersections[neighbor])
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(intersections[neighbor], intersections[goal])
                heapq.heappush(frontier, (priority, new_cost, neighbor, path + [neighbor]))

    return []