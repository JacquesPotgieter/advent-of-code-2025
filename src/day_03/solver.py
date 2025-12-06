def solve(battery_list, logging=False):
    total_joltage = 0

    for battery in battery_list:
        joltage = find_highest_joltage(battery, logging)
        total_joltage += joltage
    
    return total_joltage


def find_highest_joltage(battery, logging=False):
    battery_string = str(battery)

    if logging:
        print(f"Testing {battery=}")
    # First Pos will always be largest number, assuming second Pos is at the end
    first_pos = find_largest_value_position(battery_string[0:-1], logging)
    first_value = battery_string[first_pos]

    if logging:
        print(f"First Value= {first_value}")

    # Second Pos will always be largest number after the first Post
    remaining_string = battery_string[first_pos+1:]
    second_pos = find_largest_value_position(remaining_string, logging)
    second_value = remaining_string[second_pos]
    if logging:
        print(f"Second Value= {second_value}")
    
    joltage = int(f"{first_value}{second_value}")
    if logging:
        print(f"Final joltage is {joltage}")

    return joltage


def find_largest_value_position(list_string, logging=False):
    largest = 0
    largest_pos = 0

    for counter in range(len(list_string)):
        compare = int(list_string[counter])

        if largest < compare:
            largest = compare
            largest_pos = counter
        
    if logging:
        print(f"From {list_string} --> Largest value {largest} -- Position {largest_pos}")
    return largest_pos