# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    import numpy as np
    a = [1, 2, 3, 4, 5, 6]
    b = [10, 11, 12, 13, 14, 15]
    x = np.min((np.max(a),np.min(b)))
    print (x)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
