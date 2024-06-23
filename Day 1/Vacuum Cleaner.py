import random
import time

# Initial state: (A, B) where A and B are 0 (clean) or 1 (dirty)
def initial_state():
    A = random.randint(0, 1)
    B = random.randint(0, 1)
    return (A, B)

# Action: Suck
def suck(state, room):
    state_list = list(state)
    state_list[room] = 0
    return tuple(state_list)

# Action: Move
def move(room):
    return 1 - room  # Toggle between 0 and 1 (assuming only 2 rooms)

# Simple vacuum cleaner agent
def vacuum_cleaner():
    # Initial state
    state = initial_state()
    print("Initial State:", state)
    
    # Main loop until both rooms are clean
    while 1 in state:
        room = random.randint(0, 1)  # Choose a random room to act upon
        
        # Perform the action based on the room's state
        if state[room] == 1:
            state = suck(state, room)
            print(f"Suck in Room {chr(ord('A') + room)} -> New State: {state}")
        else:
            new_room = move(room)
            print(f"Move from Room {chr(ord('A') + room)} to Room {chr(ord('A') + new_room)}")
            time.sleep(1)  # Simulate movement delay
        print("-----------------------")
        time.sleep(1)  # Pause between actions

    print("All rooms are clean. Mission accomplished!")

# Run the vacuum cleaner agent
vacuum_cleaner()
