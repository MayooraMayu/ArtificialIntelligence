import itertools
def calculate_total_distance(route, distances):
    total_distance = 0
    num_cities = len(route)
    for i in range(num_cities):
        total_distance += distances[route[i % num_cities]][route[(i + 1) % num_cities]]
    return total_distance
distances = [
    [0, 10, 15, 20],  
    [10, 0, 35, 25],
    [15, 35, 0, 30],   
    [20, 25, 30, 0] 
]

num_cities = len(distances)
cities = list(range(num_cities))
min_distance = float('inf')
best_route = None
for route in itertools.permutations(cities):
    route_distance = calculate_total_distance(route, distances)
    if route_distance < min_distance:
        min_distance = route_distance
        best_route = route
print(f"The shortest route is: {best_route} with a total distance of {min_distance}")
