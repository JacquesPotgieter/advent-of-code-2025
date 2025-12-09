
def solve(input_tuples):
    total_value = 0

    for (start, end) in input_tuples:
        patterns = find_pattern_numbers(start, end)

        for pattern in patterns:
            total_value += pattern
    
    return total_value

def find_pattern_numbers(start, end, logging=False):
    pattern_numbers = []

    for current_num in range(start, end+1):
        if is_pattern_numberV2(current_num, logging):
            pattern_numbers.append(current_num)

    return pattern_numbers


def is_pattern_number(current_num, logging=False):
    if logging:
        print(f"Step: {current_num=} ", end="")

    num_string = str(current_num)

    if len(num_string) % 2 != 0:
        # Odd number of digits. Cannot have same pattern twice
        if logging:
            print(" -> Skip")
        return False
    
    mid_point = int(len(num_string) / 2)

    split_number_start = num_string[:mid_point]
    split_number_end = num_string[-mid_point:]

    if logging:
        print(f"{split_number_start} -- {split_number_end}", end="")

    if (split_number_start == split_number_end):
        if logging:
            print(f" -> Found")
        return True

    if logging:
        print(f" -> Skip")
    return False


def is_pattern_numberV2(current_num, logging=False):
    if logging:
        print(f"\n\nStep: {current_num=} ")

    num_string = str(current_num)
    
    split_max_size = int(len(num_string) / 2)

    if logging:
        print(f" ({split_max_size=}) ")

    for split_size in range(1, split_max_size + 1):
        is_a_pattern = True

        # Can the split_size divide it equally
        if len(num_string) % split_size != 0:
            if logging:
                print(f" (Not {split_size})")
            continue

        # Comparison against
        split_value = num_string[:split_size]
        if logging:
                print(f" ({split_value=})")

        # Get possible Splits
        split_points = _get_split_points(len(num_string), split_size)
        # split_points = [(split_size * counter, split_size * (counter + 1)) for counter in range(1, split_max_size)]
        if logging:
            print(f"Split points at {split_points}")

        if len(split_points) == 0:
            raise Exception("Split points are wrong")
        
        for (start, end) in split_points:
            split_comparison = num_string[start:end]
            if logging:
                print(f"Split comparison {split_comparison}")

            if split_value != split_comparison:
                # Exit the comparison loop. They are not equal
                is_a_pattern = False
                break
        
        if is_a_pattern:
            if logging:
                print(f"Found result with {split_size=} and {split_value=}")
            return True
    
    if logging:
        print(f"Not a pattern - {current_num}")
    return False

        
        # # How many splits will exist
        # split_number_of_them = int(len(num_string) / split_size)

        # # Get starting point to compare with
        # split_value = num_string[:split_size]
        # if logging:
        #     print(f"Compare against {split_value}")

        # # Compare against other splits
        # for counter in range(1, split_number_of_them):
        #     split_starting_point = split_size * counter
        #     split_ending_point = split_size * (counter + 1)
        #     next_split_value = num_string[split_starting_point:split_ending_point]

        #     if logging:
        #         print(f"{split_starting_point=}, {split_ending_point=}")
        #         print(f"Comparing {next_split_value}")

        #     if split_value != next_split_value:
        #         # Exit the comparison loop. They are not equal
        #         is_a_pattern = False
        #         break

        # # All comparisons succeeded, Must be pattern
        # if is_a_pattern:
        #     if logging:
        #         print(f"Found result with {split_size=} and {split_value=}")
        #     return True

            

        # for counter in range(0, )
        # split_value = num_string[:split_size]
        
        # split_compare = num_string[split_size:split_size * 2]
        # print(f"Compare {split_value} - {split_compare}")

        # split_compare = num_string[split_size*2:split_size * 3]
        # print(f"Compare {split_value} - {split_compare}")
        # for (counter in [])
        # counter = 0
        # while (counter < len(num_string)):
        #     split_parts.append()

    # Lets stick to string comparisons.
    # Each string must be able to be divided equally (2,3,4,5... equal parts)
    # Compare that all parts are equal. Break if any rule beaks


def _get_split_points(total_length, split_size):
    split_points = []

    counter = 0

    while True:
        split_start = split_size * counter
        split_end = split_size * (counter + 1)

        if (split_start > total_length or split_end > total_length):
            break
        counter += 1
        split_points.append((split_start, split_end))
    
    return split_points




