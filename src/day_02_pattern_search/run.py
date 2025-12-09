#!/usr/bin/env python

import re
from argparse import ArgumentParser
import os.path
from solver import solve

# ------------------------------------------------------------------------------------------
# ------------------ ArgParse things -------------------------------------------------------
# ------------------------------------------------------------------------------------------

parser = ArgumentParser(description="AdventOfCode 2025 - Day 02")
parser.add_argument('--use-full', dest="use_full", action='store_true')

args = parser.parse_args()

# ------------------------------------------------------------------------------------------
# ------------------ Read FILE -------------------------------------------------------------
# ------------------------------------------------------------------------------------------

input_file = "./input_file.txt"
example_file = "./example_input.txt"

def parse_file_input(use_full):
    resulting_list = []

    file_name = example_file
    if use_full:
        file_name = input_file 
    
    dirname = os.path.dirname(__file__)
    file_path = os.path.join(dirname, file_name)

    print(f"* Using Input file - {file_path}")

    with open(file_path) as f:
        file_lines = f.read().split(",")
        for line in file_lines:
            line_nums = line.split("-")
            resulting_list.append((int(line_nums[0]), int(line_nums[1])))
    
    return resulting_list


# ------------------------------------------------------------------------------------------
# ------------------ Start code ------------------------------------------------------------
# ------------------------------------------------------------------------------------------

print("-------- Start of Run - Day 02")

input_list = parse_file_input(args.use_full)
print("")

total_value = solve(input_list)

print(f"Total value = {total_value}")

print("\n -------- End of Run - Day 02")