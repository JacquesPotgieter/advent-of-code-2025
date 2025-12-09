class GridItem:
    def __init__(self, x, y, item):
        self.x = x
        self.y = y
        self.item = item

        self.neighbour_count = 0
    
    def increase(self):
        self.neighbour_count += 1


class Grid:
    def __init__(self, grid_lines, logging=False):
        self.list_of_lines = []

        # grid_lines is a list of a list
        # Outer List is Y. Inner List is X
        # [
        #   y1 = [x1, x2, x3],
        #   y2 = [x1, x2, x3],
        # ]

        for count_y in range(len(grid_lines)):
            string_grid_row = grid_lines[count_y]

            if logging:
                print(f"Count at {count_y} : ", end="")
                print(f"Row is {string_grid_row} -> ", end="")

            item_row = []
            for count_x in range(len(string_grid_row)):
                string_item = string_grid_row[count_x]

                if logging:
                    print(f"Item is {string_item} - ", end="")

                grid_item = GridItem(count_x, count_y, string_item)

                # Save the current item into Row
                item_row.append(grid_item)

            # Save the full Row into Grid
            self.list_of_lines.append(item_row)

            if logging:
                print(f"(Length is at {len(self.list_of_lines)})", end="")
                print()

        self.total_length_y = len(self.list_of_lines)
        self.total_length_x = len(self.list_of_lines[0])

        if logging:
            print(f"( X Length is at {self.total_length_y} : ", end="")
            print(f"Y Length is at {self.total_length_y} )", end="")
            print()
    

    def get(self, x, y):
        row = self.list_of_lines[y]
        value = row[x]

        return value


    def _safe_update(self, x, y, logging=False):
        if logging:
            print(f"Updating at ({x}, {y}) -> ", end="")

        if y < self.total_length_y and y >= 0:
            if x < self.total_length_x and x >= 0:
                item = self.get(x, y)
                item.increase()
                if logging:
                    print(f"Updated to {item.neighbour_count}", end="")

        if logging:
            print()

    def update_neighbours(self, x, y, logging=False):
        self._safe_update(x - 1, y - 1, logging) # Top left
        self._safe_update(x    , y - 1, logging) # Top middle
        self._safe_update(x + 1, y - 1, logging) # Top right

        self._safe_update(x - 1, y   , logging) # Middle left
        self._safe_update(x + 1, y   , logging) # Middle right

        self._safe_update(x - 1, y + 1, logging) # Bottom left
        self._safe_update(x    , y + 1, logging) # Bottom middle
        self._safe_update(x + 1, y + 1, logging) # Bottom right

    def cleanup_neighbours(self, with_count_below):
        for y in range(self.total_length_y):
            for x in range(self.total_length_x):
                item = self.get(x, y)

                if item.neighbour_count < with_count_below:
                    item.item = "x"

                item.neighbour_count = 0


    def process_list(self, with_count_below):
        total_count = 0

        for y in range(self.total_length_y):
            for x in range(self.total_length_x):
                item = self.get(x, y)

                if item.item == "@":
                    if item.neighbour_count < with_count_below:
                        total_count += 1
        
        return total_count



    def print(self):
        print(f"Grid is:")
        for y in range(self.total_length_y):
            print(f"-- ", end="")
            for x in range(self.total_length_x):
                item = self.get(x, y)
                print(f"{item.item}", end="")
            print()
        print("-------------")
    
    def print_count(self):
        print(f"Neighbour count is:")
        for y in range(self.total_length_y):
            print(f"-- ", end="")
            for x in range(self.total_length_x):
                item = self.get(x, y)
                print(f"{item.neighbour_count}", end="")
            print()
        print("-------------")
    
    def print_count_under(self, value):
        print(f"Replacing neighbour over {value}:")
        for y in range(self.total_length_y):
            print(f"-- ", end="")
            for x in range(self.total_length_x):
                item = self.get(x, y)
                
                item_to_print = item.item

                if item.item == "@":
                    if item.neighbour_count < value:
                        item_to_print = "x"

                print(f"{item_to_print}", end="")
            print()
        print("-------------")
