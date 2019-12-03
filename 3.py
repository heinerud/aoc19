import collections
import sys


MOVE_MAP = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}


def moves(line):
    return line.split(",")


def move(positions, m):
    v = MOVE_MAP[m[0]]
    length = int(m[1:])

    for _ in range(length):
        pos = positions[-1]
        positions.append((pos[0] + v[0], pos[1] + v[1]))

    return positions


def ack_intersection_distance(routes, intersection):
    distances = [route.index(intersection) for route in routes]
    return sum(distances)


lines = [x for x in sys.argv[1:]]

routes = []
for line in lines:
    route_positions = [(0, 0)]
    for m in moves(line):
        route_positions = move(route_positions, m)
    routes.append(route_positions)

all_positions = [position for route in routes for position in route]
intersection_candidates = [
    x for x, count in collections.Counter(all_positions).items() if count > 1
]
intersections = []
set_routes = [set(x) for x in routes]  # Performance boost
for candidate in intersection_candidates:
    if all([candidate in route for route in set_routes]):
        intersections.append(candidate)
intersections.remove((0, 0))

intersection_distances_from_origo = [abs(x) + abs(y) for x, y in intersections]
print(min(intersection_distances_from_origo))

combined_route_distances_from_origo = [
    ack_intersection_distance(routes, x) for x in intersections
]
print(min(combined_route_distances_from_origo))
