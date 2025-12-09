from grid import Grid

def solve(list_of_strings, verbose=True):
    grid = Grid(list_of_strings)

    print("File has been read")

    if verbose:
        grid.print()
    
    print("Grid has been updated")

    if verbose:
        grid.print_count_under(4)
    
    number_runs = 0
    total_count = 0

    while True:
        process_below = 4

        print(f"Process #{number_runs} -> ", end="")

        for y in range(grid.total_length_y):
            for x in range(grid.total_length_x):
                item = grid.get(x, y)

                if item.item == "@":
                    grid.update_neighbours(x, y)

        updated_count = grid.process_list(process_below)
        print(f"Updated count = {updated_count}", end="")

        if updated_count > 0:
            number_runs += 1
            total_count += updated_count
            grid.cleanup_neighbours(process_below)
            print(f" -> Going again.")

        else:
            print()
            break

    
    
    print(f"Number of runs = {number_runs}")

    return total_count