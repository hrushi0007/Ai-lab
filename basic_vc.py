# Vacuum Cleaner Agent with Percept Sequence Tracking

def vacuum_agent(percept):
    location, status = percept
    if status == "Dirty":
        return "SUCK"
    elif location == "A":
        return "RIGHT"
    else:
        return "LEFT"


# Environment
rooms = {
    "A": "Dirty",
    "B": "Dirty"
}

total_rooms = len(rooms)
cleaned_rooms = 0
current_location = "A"

percept_sequence = []  # stores percept history

print("\nStep | Location | Action | Status | Performance | Percentage | Percept Sequence")
print("--------------------------------------------------------------------------------")

# Run agent for more steps (increased sequence)
for step in range(1, 7):
    status = rooms[current_location]
    percept = (current_location, status)

    # Add percept to percept sequence
    percept_sequence.append(percept)

    action = vacuum_agent(percept)

    # Perform action
    if action == "SUCK":
        if rooms[current_location] == "Dirty":
            rooms[current_location] = "Clean"
            cleaned_rooms += 1

    elif action == "RIGHT":
        current_location = "B"

    elif action == "LEFT":
        current_location = "A"

    performance = cleaned_rooms
    percentage = (cleaned_rooms / total_rooms) * 100

    print(f"{step:^4} | {current_location:^8} | {action:^6} | "
          f"{rooms[current_location]:^6} | {performance:^11} | "
          f"{percentage:^9.0f}% | {percept_sequence}")
