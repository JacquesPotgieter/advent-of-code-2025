from solver import find_highest_joltage_v2, find_largest_value_position

def test_find_largest_value_position(list_string, start, end, expected):
    print(f"* (Testing {list_string=} between Pos ({start} & {end}) with {expected=}")
    result = find_largest_value_position(list_string, start, end)
    assert result == expected, f"({list_string=}) between Pos ({start} & {end}) {expected=}, but returned {result}"

def test_find_highest_joltage(battery, size, expected, logging=False):
    print(f"* (Testing {battery=}) with {expected=}")
    result = find_highest_joltage_v2(battery, size, logging)
    assert result == expected, f"({battery=}) {expected=}, but returned {result}"

print("find_largest_value_position --> ")
test_find_largest_value_position("0123456", 0, 6, 6)
test_find_largest_value_position("0123456", 0, 4, 4)
test_find_largest_value_position("6543210", 0, 6, 0)
test_find_largest_value_position("6543210", 2, 6, 2)


print("\n find_highest_joltage --> ")
test_find_highest_joltage(9876, 2, 98)
test_find_highest_joltage(1234, 2, 34)
test_find_highest_joltage(119811, 2, 98)

test_find_highest_joltage(9876, 3, 987)
test_find_highest_joltage(1234, 3, 234)
test_find_highest_joltage(1198119, 3, 989)
