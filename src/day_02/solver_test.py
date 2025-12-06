from solver import find_pattern_numbers, is_pattern_numberV2

def test(start, end, expected):
    print(f"* (Testing {start=}, {end=}) with {expected=}")
    result = find_pattern_numbers(start, end)
    assert result == expected, f"({start=}, {end=}) {expected=}, but returned {result}"

def test_is_pattern_number(value, expected, logging=False):
    print(f"* (Testing {value=}) with {expected=}")
    result = is_pattern_numberV2(value, logging)
    assert result == expected, f"({value=}), {expected=}, but returned {result}"

print("-------- Starting tests now\n")

test(11, 22, [11, 22])
test(8, 15, [11])
test(998, 1012, [1010])
test(38593856, 38593862, [38593859])

print()
test_is_pattern_number(1211_1211, True)
test_is_pattern_number(1211_3_1211, False)
test_is_pattern_number(1_1_1_1_1_1_1, True)
test_is_pattern_number(123_123_123, True)
test_is_pattern_number(123_123_125, False)


print("-------- All tests succeeded")
