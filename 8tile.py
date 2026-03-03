import heapq

GOAL_STATE = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

MOVES = {
    "Up": (-1, 0),
    "Down": (1, 0),
    "Left": (0, -1),
    "Right": (0, 1)
}

def manhattan_distance(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x = (val - 1) // 3
                goal_y = (val - 1) % 3
                dist += abs(i - goal_x) + abs(j - goal_y)
    return dist

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
def get_neighbors(state):
    neighbors = []
    x, y = find_zero(state)

    for move, (dx, dy) in MOVES.items():
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append((tuple(map(tuple, new_state)), move))
    return neighbors

def a_star(start):
    pq = []
    heapq.heappush(pq, (0, start, []))
    visited = set()

    while pq:
        cost, state, path = heapq.heappop(pq)

        if state == GOAL_STATE:
            return path

        if state in visited:
            continue
        visited.add(state)

        for neighbor, move in get_neighbors(state):
            if neighbor not in visited:
                g = len(path) + 1
                h = manhattan_distance(neighbor)
                heapq.heappush(pq, (g + h, neighbor, path + [(neighbor, move)]))

    return None
def print_board(state):
    for row in state:
        print(" ".join(str(x) if x != 0 else "_" for x in row))
    print()
print("Enter the initial state (use 0 for empty tile):")
start = []
for i in range(3):
    row = list(map(int, input().split()))
    start.append(tuple(row))

start_state = tuple(start)

solution = a_star(start_state)
if solution:
    print("\nOptimal Solution Found!\n")
    print("Initial State:")
    print_board(start_state)

    step = 1
    for state, move in solution:
        print(f"Step {step}: Move {move}")
        print_board(state)
        step += 1

    print("Total moves:", len(solution))
else:
    print("No solution exists.")
