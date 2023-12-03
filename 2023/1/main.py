# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # read input file
    # for each line:
    #   parse through each character
    #   discard letters
    #   save first number to 0 of calibration value array
    #   save last number to 1
    #   add both numbers to new total variable
    # print result after finishing last line

    calib = [0, 0]
    input = open('input', 'r', encoding="utf-8")

    for line in input:
        chars = list(line)
        for char in chars:
            if char !=


        # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
