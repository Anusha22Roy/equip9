from collections import deque

def find_nearest_equipment(n, edges, availability, start_provider, target_equipment):
    # Build adjacency list
    graph = {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # BFS setup
    queue = deque([(start_provider, [start_provider])])  # (current_provider, path)
    visited = set()
    visited.add(start_provider)

    while queue:
        provider, path = queue.popleft()

        # Check if this provider has the required equipment
        if target_equipment in availability.get(provider, []):
            return path  # Return the shortest path to this provider
        
        # Explore neighbors
        for neighbor in graph.get(provider, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return -1  # No provider with the required equipment found

# Example usage
n = 5
edges = [(1, 2), (2, 3), (3, 4), (4, 5)]
availability = {1: ["excavator"], 2: [], 3: ["bulldozer"], 4: ["excavator"], 5: ["crane"]}
start_provider = 2
target_equipment = "excavator"

print(find_nearest_equipment(n, edges, availability, start_provider, target_equipment))