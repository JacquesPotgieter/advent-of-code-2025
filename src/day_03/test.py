from solver import find_highest_joltage, find_largest_value_position

def test_find_largest_value_position(list_string, expected):
    print(f"* (Testing {list_string=}) with {expected=}")
    result = find_largest_value_position(list_string)
    assert result == expected, f"({list_string=}) {expected=}, but returned {result}"

def test_find_highest_joltage(battery, expected, logging=False):
    print(f"* (Testing {battery=}) with {expected=}")
    result = find_highest_joltage(battery, logging)
    assert result == expected, f"({battery=}) {expected=}, but returned {result}"

print("find_largest_value_position --> ")
test_find_largest_value_position("123", 2)
test_find_largest_value_position("132", 1)
test_find_largest_value_position("321", 0)


print("\n find_highest_joltage --> ")
test_find_highest_joltage(9876, 98)
test_find_highest_joltage(1234, 34)
test_find_highest_joltage(119811, 98)
