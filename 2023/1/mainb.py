"""
Solution to problem 1b of Advent of Code 2023
Approach to this should be removing the first_value bool etc. and instead storing integer values in a dynamic list.
This way, we can also iterate over strings in each line and check if they are the same as the name of an integer,
and if they are, add them to the list.
To make searching through the string easier, I will import the re (regex) module and search this way.
Update 02/12 - approach will now be to search each line in turn with regex, map words to integers, and save all words
and implicit integer cases as I go. Then, pick first and last values and use as in part a.
"""

import re


def print_hi():
    print(f"test1")
    values = list  # list of possible calibration values. values[0] will always be set as calib[0]
    calib = list  # Calibration values [1, n-1] to store from a list of n values
    current = ""  # Current string being stored and searched
    input_file = open('input.txt', 'r', encoding="utf-8")  # Reading the input.txt file
    calib_total = 0  # The calibration values' total representation (put together as an int, i.e. [a,b] => ab)
    total = 0  # the overall total of values, used in problems 1a and 1b.

    number_map = {  # A dictionary mapping each english number name to its digit representation
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    for line in input_file:  # For each line:
        print(f"The current line being read is:   " + line)
        values = re.compile(r'(?:\b(?:' + '|'.join(map(re.escape(), number_map(line))) + r')\b|\d)')  # Regex stuff
        calib[0] = values[0]
        calib[1] = values[-1]

        print(f"The calibration values are: " + str(calib))
        calib_total = int(str(calib[0]) + str(calib[1]))
        total += calib_total
        print(f"The final calibration value of line " + line + " is: " + str(calib_total))
        print(f"The sum total of all calibration values so far is: " + str(total))

    print(f"Test")


if __name__ == '__mainb__':
    print(f"test3")
    print_hi()
