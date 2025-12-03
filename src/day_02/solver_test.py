from solver import find_pattern_numbers

def test(start, end, expected):
    print(f"* (Testing {start=}, {end=}) with {expected=}")
    result = find_pattern_numbers(start, end)
    assert result == expected, f"({start=}, {end=}) {expected=}, but returned {result}"

print("-------- Starting tests now. No response means success\n")

test(11, 22, [11, 22])
test(8, 15, [11])
test(998, 1012, [1010])
test(38593856, 38593862, [38593859])


print("-------- All tests succeeded")
