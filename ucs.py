import heapq

# 7-Level Graph
graph = {
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 3)],
    'C': [],
    'D': [('E', 2)],
    'E': [('F', 4), ('H', 6)],
    'F': [('I', 1)],
    'H': [],
    'I': [('J', 2)],
    'J': []
}

def uniform_cost_search(start, goal):
    frontier = []
    heapq.heappush(frontier, (0, start, [start]))
    explored = set()
    level = 0

    while frontier:
        print("\n----------------------------")
        print("LEVEL:", level)
        print("Frontier:", frontier)
        print("Explored:", explored)

        cost, current, path = heapq.heappop(frontier)
        print("Expanding:", current, " Cost:", cost)

        if current == goal:
            print("\n✅ Goal Found")
            print("Path:", path)
            print("Total Cost:", cost)
            return

        explored.add(current)

        for neighbor, weight in graph.get(current, []):
            if neighbor not in explored:
                heapq.heappush(frontier, (cost + weight, neighbor, path + [neighbor]))

        level += 1

    print("❌ Goal not reachable")


# Driver
start_node = 'A'
goal_node = 'J'
uniform_cost_search(start_node, goal_node)
