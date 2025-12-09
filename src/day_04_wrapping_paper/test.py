from grid import Grid

def test_grid(list_of_strings, expected_x, expected_y, expected_value, logging=False):
    print(f"* (Testing Grid) with ({expected_x=} {expected_y=} {expected_value=}) and grid {list_of_strings}")
    result = Grid(list_of_strings, logging)

    result_item = result.get(expected_x, expected_y).item
    assert result_item == expected_value, f"Value at ({expected_x}, {expected_y}) expected {expected_value}, but returned {result_item})"


def test_verify_neighbour(grid, expected_x, expected_y, expected_value, logging=False):
    print(f"* (Testing update) with ({expected_x=} {expected_y=} {expected_value=}) and grid {grid}")

    result_item = grid.get(expected_x, expected_y).neighbour_count
    assert result_item == expected_value, f"Value at ({expected_x}, {expected_y}) expected {expected_value}, but returned {result_item})"


print("Test Grid")
grid_string = [
    "123",
    "456",
    "789",
    "012",
]
test_grid(grid_string, 0, 0, "1")
test_grid(grid_string, 2, 0, "3")
test_grid(grid_string, 0, 2, "7")

print()

print("Update Neighbour")

grid = Grid(grid_string)

assert grid.total_length_x == 3, f"Grid length is wrong. Expected 3, but was {grid.total_length_x}"
assert grid.total_length_y == 4, f"Grid length is wrong. Expected 3, but was {grid.total_length_y}"

# Update corner
grid.update_neighbours(0, 0)
test_verify_neighbour(grid, 0, 0, 0) # Itself should be zero
test_verify_neighbour(grid, 1, 0, 1) # One row down should be one
test_verify_neighbour(grid, 2, 0, 0) # Two row down should be zero
test_verify_neighbour(grid, 1, 1, 1) # One diagonal down should be one

# Updating middle now
grid.update_neighbours(1, 1)
test_verify_neighbour(grid, 1, 1, 1) # Itself should be one
test_verify_neighbour(grid, 0, 0, 1) # Corner should be one
test_verify_neighbour(grid, 2, 0, 1) # Top Corner should be one
test_verify_neighbour(grid, 1, 0, 2) # Top middle should be two
test_verify_neighbour(grid, 0, 1, 2) # Middle left should be two

print()

grid.print()
grid.print_count()