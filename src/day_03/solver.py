def solve(battery_list, logging=False):
    total_joltage = 0

    for battery in battery_list:
        joltage = find_highest_joltage(battery, 12, logging)
        total_joltage += joltage
    
    return total_joltage


def find_highest_joltage(battery, battery_size, logging=False):
    battery_string = str(battery)
    battery_total_length = len(battery_string)

    battery_joltage = ""

    if logging:
        print(f"Testing {battery=}")
        print(f"Looking for size - {battery_size}")
    
    battery_start_pos = 0

    for batteries_remaining in range(battery_size, 0, -1):
        # We need at least Count positions for remaining values
        battery_end_post = battery_total_length - batteries_remaining

        # Next highest battery is at Pos
        found_position = find_largest_value_position(battery_string, battery_start_pos, battery_end_post)

        # Update starting search to exclude latest found Pos
        battery_start_pos = found_position + 1

        # Battery Value
        battery_joltage = f"{battery_joltage}{battery_string[found_position]}"
    
    return int(battery_joltage)


def find_largest_value_position(list_string, search_start_pos, search_end_pos, logging=False):
    largest = 0
    largest_pos = 0

    for counter in range(search_start_pos, search_end_pos + 1):
        compare = int(list_string[counter])

        if largest < compare:
            largest = compare
            largest_pos = counter
        
    if logging:
        print(f"From {list_string} --> Largest value {largest} -- Position {largest_pos}")
    return largest_pos