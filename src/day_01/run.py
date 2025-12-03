#!/usr/bin/env python

import re
from argparse import ArgumentParser
import os.path

from lock_position import LockPosition



def main(input_list):
    lock_position = LockPosition()

    for change in input_list:
        message = f"{change} : {lock_position.position} ->"
        
        clean_text = re.sub(r'\D', '', change)
        num = int(clean_text)

        increase = change[0] == "R"
        if increase:
            lock_position.increase(num)
        else:
            lock_position.decrease(num)

        message = f"{message} {lock_position.position}"
        print(message)
    
    print(f"Password is {lock_position.password_count}")


# ------------------------------------------------------------------------------------------
# ------------------ ArgParse things -------------------------------------------------------
# ------------------------------------------------------------------------------------------

def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')  # return an open file handle


parser = ArgumentParser(description="AdventOfCode 2025 - Day 01")
parser.add_argument("-i", dest="filename", required=True,
                    help="input file with instructions", metavar="FILE",
                    type=lambda x: is_valid_file(parser, x))
args = parser.parse_args()

# ------------------------------------------------------------------------------------------
# ------------------ Start code ------------------------------------------------------------
# ------------------------------------------------------------------------------------------

print("-------- Start of Run - Day 01")

input_list = [line.rstrip() for line in args.filename]
# input_list = list(args.filename)
main(input_list)

print("\n -------- End of Run - Day 01")