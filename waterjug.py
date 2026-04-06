from collections import deque

# Capacities
capacity = (12, 8, 5, 3)

# Initial and goal states
initial = (12, 0, 0, 0)
goal = (6, 6, 0, 0)

def get_next_states(state):
    states = []
    for i in range(4):
        for j in range(4):
            if i != j:
                s = list(state)
                # Pour from i to j
                transfer = min(s[i], capacity[j] - s[j])
                s[i] -= transfer
                s[j] += transfer
                states.append(tuple(s))

    # Empty each jug
    for i in range(4):
        s = list(state)
        s[i] = 0
        states.append(tuple(s))

    return states

def bfs():
    queue = deque([[initial]])
    visited = set()

    while queue:
        path = queue.popleft()
        state = path[-1]

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for next_state in get_next_states(state):
            if next_state not in visited:
                queue.append(path + [next_state])

    return None

solution = bfs()

if solution:
    print("Solution Path:")
    for step in solution:
        print(step)
else:
    print("No solution found")
