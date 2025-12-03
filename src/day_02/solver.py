
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
        if logging:
            print(f"Step: {current_num=} ", end="")

        num_digits = str(current_num)

        if len(num_digits) % 2 != 0:
            # Odd number of digits. Cannot have same pattern twice
            if logging:
                print(" -> Skip")
            continue
        
        mid_point = int(len(num_digits) / 2)

        split_number_start = num_digits[:mid_point]
        split_number_end = num_digits[-mid_point:]

        if logging:
            print(f"{split_number_start} -- {split_number_end}", end="")

        if (split_number_start == split_number_end):
            pattern_numbers.append(current_num)
            if logging:
                print(f" -> Found")
            continue

        if logging:
            print(f" -> Skip")
        

    return pattern_numbers






