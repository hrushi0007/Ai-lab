import random

# -----------------------------
# 1. INITIAL ROOMS AND PARTS
# -----------------------------
rooms = {
    "Room1": {"Left": "Dirty", "Right": "Dirty"},
    "Room2": {"Left": "Dirty", "Right": "Dirty"},
    "Room3": {"Left": "Dirty", "Right": "Dirty"}
}

# Randomly assign dirt
for room in rooms:
    for part in rooms[room]:
        rooms[room][part] = random.choice(["Clean", "Dirty"])

room_names = list(rooms.keys())
current_room_index = 0
current_part = "Left"

performance_score = 0
step = 0
percept_sequence = []

# -----------------------------
# HELPER FUNCTIONS
# -----------------------------
def room_clean_percentage(rooms):
    total_parts = len(rooms) * 2
    clean_parts = sum(
        1 for room in rooms.values() for part in room.values() if part == "Clean"
    )
    return int((clean_parts / total_parts) * 100)


def all_rooms_clean(rooms):
    return all(part == "Clean" for room in rooms.values() for part in room.values())


# -----------------------------
# TABLE HEADER
# -----------------------------
print("\nSTEP | LOCATION | PERCEPT STATUS | ACTION | PERFORMANCE | PERCENTAGE | PERCEPT SEQUENCE")
print("-------------------------------------------------------------------------------------------")

# -----------------------------
# AGENT LOOP
# -----------------------------
while not all_rooms_clean(rooms):
    step += 1
    current_room = room_names[current_room_index]
    status = rooms[current_room][current_part]

    percept = (current_room, current_part, status)
    percept_sequence.append(percept)

    # Agent decision
    if status == "Dirty":
        action = "SUCK"
        rooms[current_room][current_part] = "Clean"
        performance_score += 10
    else:
        action = "MOVE"
        performance_score += 5
        # switch part or move to next room
        if current_part == "Left":
            current_part = "Right"
        else:
            current_part = "Left"
            current_room_index = (current_room_index + 1) % len(room_names)

    percentage = room_clean_percentage(rooms)

    print(f"{step:^4} | {current_room:^8} | {current_part:^14} | "
          f"{action:^6} | {performance_score:^11} | {percentage:^10}% | {percept_sequence}")

# -----------------------------
# FINAL OUTPUT
# -----------------------------
print("\n✅ All rooms and all parts are completely cleaned.")
print("🤖 Thank you for using LUNA AI Vacuum Cleaner.")