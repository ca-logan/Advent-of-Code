# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    calib = list  #Calibration values to store
    first_value = False #Boolean telling us whether the first calibration value has been read
    current_value = 0   #The current int value (note: this isn't doing anything unless it's the first or last int
    input = open('input.txt', 'r', encoding="utf-8")    #Reading the input.txt file
    calib_total = 0 #The calibration values' total representation (put together as an int, i.e. [a,b] => ab)
    total = 0

    for line in input:                      #For each line, read each character
        chars = list(line)
        calib = [0,0]
        current_value = 0
        calib_total = 0
        first_value = False
        second_value = False
        for char in chars:                  #For each character, check if it's an integer value
            try:
                current_value = int(char)
                print(f"The character being checked was an integer: " + char)
                if not first_value:    #If it is, and we've not yet read the first value, set accordingly
                    first_value = True
                    calib[0] = current_value
                    print(f"The first calibration value on line " + line + " is: " + char)
                elif first_value == True:    #If we have read the first value
                    second_value = True
                    calib[1] = current_value    #Set the current value as the final calibration value
            except ValueError:
                print(f"ValueError: The character being checked wasn't an integer value: " + char)
        if not second_value:
            calib[1] = calib[0]
        print(f"the second calibration value on line " + line + " is: " + str(current_value))
        print(f"The calibration values are: " + str(calib))
        calib_total = int(str(calib[0]) + str(calib[1]))
        total += calib_total
        print(f"The final calibration value of line " + line + " is: " + str(calib_total))
        print(f"The sum total of all calibration values so far is: " + str(total))

        # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
