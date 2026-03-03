import heapq

START_STATE = ("left", "middle", False, False)
GOAL_STATE = ("middle", "middle", True, True)

POSITIONS = ["left", "middle", "right"]

def heuristic(state):
    monkey_pos, box_pos, on_box, has_banana = state

    if has_banana:
        return 0

    h = 0
    if monkey_pos != box_pos:
        h += 1
    if box_pos != "middle":
        h += 1
    if not on_box:
        h += 1
    return h

def get_neighbors(state):
    monkey_pos, box_pos, on_box, has_banana = state
    neighbors = []

    # Move monkey
    if not on_box:
        for pos in POSITIONS:
            if pos != monkey_pos:
                neighbors.append((pos, box_pos, False, has_banana))

    # Push box
    if monkey_pos == box_pos and not on_box:
        for pos in POSITIONS:
            if pos != box_pos:
                neighbors.append((pos, pos, False, has_banana))

    # Climb box
    if monkey_pos == box_pos and not on_box:
        neighbors.append((monkey_pos, box_pos, True, has_banana))

    # Grab banana
    if monkey_pos == "middle" and box_pos == "middle" and on_box:
        neighbors.append((monkey_pos, box_pos, on_box, True))

    return neighbors

def a_star(start):
    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start, []))
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == GOAL_STATE:
            return path + [state]

        if state in visited:
            continue
        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor)
                heapq.heappush(
                    pq,
                    (new_f, new_g, neighbor, path + [state])
                )

    return None

# ---------- MAIN ----------
solution = a_star(START_STATE)

if solution:
    print("\nOptimal Solution Found!\n")
    print("Initial State:")
    print(solution[0])

    step = 1
    for state in solution[1:]:
        print(f"Step {step}:")
        print(state)
        step += 1

    print("\nTotal steps:", len(solution) - 1)
else:
    print("No solution exists.")
