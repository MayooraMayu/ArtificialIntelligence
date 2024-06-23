def water_jug_problem(jug1_capacity, jug2_capacity, target):
    jug1_current = 0
    jug2_current = 0
    print(f"Water Jug Problem with capacities {jug1_capacity} and {jug2_capacity} to measure {target} liters:")
    while True:
        print(f"Current state: ({jug1_current} liters in Jug 1, {jug2_current} liters in Jug 2)")
        if jug1_current == target or jug2_current == target:
            print(f"Solution found: {jug1_current} liters in Jug 1 and {jug2_current} liters in Jug 2.")
            return True
        if jug1_current == 0:
            jug1_current = jug1_capacity
            print(f"Fill Jug 1: ({jug1_current}/{jug2_current})")
        elif jug1_current > 0 and jug2_current < jug2_capacity:
            pour_amount = min(jug1_current, jug2_capacity - jug2_current)
            jug1_current -= pour_amount
            jug2_current += pour_amount
            print(f"Pour from Jug 1 to Jug 2: ({jug1_current}/{jug2_current})")
        elif jug2_current == jug2_capacity:
            jug2_current = 0
            print(f"Empty Jug 2: ({jug1_current}/{jug2_current})")
        elif jug2_current > 0 and jug1_current < jug1_capacity:
            pour_amount = min(jug2_current, jug1_capacity - jug1_current)
            jug2_current -= pour_amount
            jug1_current += pour_amount
            print(f"Pour from Jug 2 to Jug 1: ({jug1_current}/{jug2_current})")
        print("Continue...\n")
    print("No solution found.")
    return False
jug1_capacity = 4
jug2_capacity = 3
target = 2
water_jug_problem(jug1_capacity, jug2_capacity, target)
