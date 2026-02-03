from collections import deque

print("Define Graph G = (V, E)")

V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

graph = {}
edges_list = []

print("Enter edges (u v):")
for _ in range(E):
    u, v = input().split()

    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []

    graph[u].append(v)
    graph[v].append(u)
    edges_list.append((u, v))

# ---------------- INPUT SOURCE & GOAL ----------------
source = input("\nEnter source node: ")
goal = input("Enter goal node: ")

vertices = sorted(graph.keys())

print("\nSource Node:", source)
print("Vertices (V):", vertices)
print("Edges (E):", edges_list)

# ---------------- BFS INITIALIZATION ----------------
visited = []
queue = deque([source])
parent = {source: None}
step = 1

# ---------------- BFS TRAVERSAL ----------------
while queue:
    current = queue.popleft()

    if current not in visited:
        visited.append(current)

    # Find child vertices
    children = []
    edge_from_current = []

    for neighbor in graph[current]:
        edge_from_current.append((current, neighbor))
        if neighbor not in visited and neighbor not in queue:
            queue.append(neighbor)
            parent[neighbor] = current
            children.append(neighbor)

    unvisited = [v for v in vertices if v not in visited]

    # ---------------- STEP DISPLAY ----------------
    print(f"\nStep {step}:")
    print("Visiting Node:", current)
    print("Visited Nodes:", visited)
    print("Unvisited Nodes:", unvisited)
    print("Child Vertices:", children)
    print("Edges from current node:", edge_from_current)

    step += 1

    if current == goal:
        break

# ---------------- FINAL OUTPUT ----------------
print("\n-----------------------------")
print("Final Visited Nodes (BFS Order):", visited)
print("Non-Visited Nodes:", len(vertices) - len(visited))

# ---------------- PATH FINDING ----------------
path = []
node = goal

if node in parent:
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()
    print("Path of", source + ":", " → ".join(path))
else:
    print("No path exists.")
